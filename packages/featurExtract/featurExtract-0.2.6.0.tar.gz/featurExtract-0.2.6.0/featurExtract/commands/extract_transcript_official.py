# -*- coding: utf-8 -*-
import sys
import gffutils
import pandas as pd 
from tqdm import tqdm 
from Bio import SeqIO
from Bio.Seq import Seq
from multiprocessing import Pool
from Bio.SeqRecord import SeqRecord
from collections import defaultdict, deque
from featurExtract.database.database import create_db
from featurExtract.utils.util import add_stop_codon, mRNA_type, seq_upper_lower, parse_output

'''
https://www.ncbi.nlm.nih.gov/genbank/genomes_gff/
'''
def stop_codon(db, transcript, genome):
    s = ''
    for codon in db.children(transcript, featuretype='stop_codon', order_by='start'):
        s = codon.sequence(genome, use_strand=False) # 不反向互补,序列全部连接后再互补
    return s


def anchor_CDS(db, genome, transcript, style):
    '''
    parameters: 
     db : database create by gffutils
     transcript: gffutils transcript feature type
     style: database file type
    return:
     start_codon position 
     stop_codon positiopn 
     cds length 
    '''
    if style == 'GTF':
        start_codon_s, stop_codon_e = 0, 0
        cds = ''
        for c in db.children(transcript, featuretype='CDS', order_by='start'):
            cds += c.sequence(genome, use_strand=False)
        cds = Seq(cds)
        if transcript.strand == '-':
            cds = cds.reverse_complement()
        cds_len = len(cds) + 3 # add stop codon length
        if transcript.strand == '-':
            for i in db.children(transcript, featuretype='start_codon', order_by='start'):
                start_codon_s = i.end - 1
                start_codon_e = i.start - 1
            for i in db.children(transcript, featuretype='stop_codon', order_by='start'):
                stop_codon_s = i.end - 1
                stop_codon_e = i.start - 1  
        else:
            # contain + .
            for i in db.children(transcript, featuretype='start_codon', order_by='start'):
                start_codon_s = i.start - 1
                start_codon_e = i.end -1 
            for i in db.children(transcript, featuretype='stop_codon', order_by='start'):
                stop_codon_s = i.start - 1
                stop_codon_e = i.end -1 
         
        return start_codon_s, stop_codon_e, cds_len
    elif style == 'GFF':
        start_codon_s, stop_codon_e = 0, 0
        cds = ''
        for c in db.children(transcript, featuretype='CDS', order_by='start'):
            cds += c.sequence(genome, use_strand=False)
        cds = Seq(cds)
        if transcript.strand == '-':
            cds = cds.reverse_complement()
        cds_len = len(cds) # cds full length
        if transcript.strand == '-':
            for i in db.children(transcript, featuretype='five_prime_UTR', order_by='start'):
                # occasionally a transcript has more then one three_prime_UTR
                # occasionally a transcript do not have three_prime_UTR, start_codon_s = first exon
                # the first five_prime_UTR position should be saved in minus strand
                if i:
                    start_codon_s = i.start - 1
                    start_codon_e = i.start - 3
                    break
                else:
                    print('five_prime_UTR does not exist')
                break
            for i in db.children(transcript, featuretype='three_prime_UTR', order_by='start'):
                # occasionally a transcript has more then one three_prime_UTR
                # occasionally a transcript do not have three_prime_UTR 
                # the last save (position large)
                if i:
                    stop_codon_s = i.end - 1
                    stop_codon_e = i.end - 3
                else:
                    print('three_prime_UTR does not exist')
            if start_codon_s == 0:
                pass # five_prime_UTR does not exist
            if stop_codon_e == 0 :
                pass # three_prime_UTR does not exist  
        else:
            # contain + .
            for i in db.children(transcript, featuretype='five_prime_UTR', order_by='start'):
                # occasionally a transcript has more then one three_prime_UTR
                # occasionally a transcript do not have three_prime_UTR, start_codon_s = first exon
                # the last five_prime_UTR position should be saved in plus strand
                if i:
                    start_codon_s = i.end + 1
                    start_codon_e = i.end + 3
                else:
                    print('five_prime_UTR does not exist')
            for i in db.children(transcript, featuretype='three_prime_UTR', order_by='start'):
                # occasionally a transcript has more then one three_prime_UTR
                # the first three_prime_UTR position should be saved in plus strand
                if i:
                    stop_codon_s = i.start - 3 
                    stop_codon_e = i.start - 1
                    break 
                else:
                    print('three_prime_UTR does not exist')
        
        return start_codon_s, stop_codon_e, cds_len


_CSV_HEADER = ['TranscriptID', 'Chrom', 'Start_genome', \
               'End_genome','Start_transcript', \
               'End_transcript','Strand','CDS']

def sub_transcript(params):
    """
    parameters:
        params: argparse
    return:
        transcript_seq_list, a deque
    """
    t, database, genome, style, upper, output_format = params
    db = gffutils.FeatureDB(database, keep_order=True) # load database
    transcript_seq_list = deque()
    start_codon_s, stop_codon_e, cds_len = anchor_CDS(db, genome, t, style)
    atg2firstexon = 0
    seq = ''
    for e in db.children(t, featuretype='exon', order_by='start'):
        # 不反向互补，对于负链要得到全部的cds后再一次性反向互补
        s = e.sequence(genome, use_strand=False)
        seq += s
        if t.strand == '-':
            if start_codon_s == 0:
                # five prime_UTR not exist
                atg2firstexon = 0
            else:
                if e.start >= start_codon_s :
                    atg2firstexon += len(s)
                elif e.start < start_codon_s < e.end:
                    truncated = e.end - start_codon_s #  反向减法
                    atg2firstexon += truncated
        else:
            # contain + .
            if start_codon_s == 0:
                # five prime_UTR not exist
                atg2firstexon = 0
            else:
                if start_codon_s >= e.end:
                    atg2firstexon += len(s)
                elif e.end > start_codon_s > e.start:
                    truncated = start_codon_s - e.start
                    atg2firstexon += truncated
    seq = Seq(seq)
    if t.strand == '-':
        seq = seq.reverse_complement()
    if upper:
        seq = seq_upper_lower(seq, atg2firstexon, atg2firstexon + cds_len)
    # position in transcript 1 based 
    cds_start_transcript = atg2firstexon + 1
    cds_end_transcript = atg2firstexon + cds_len
    if output_format == 'fasta':
        desc='strand:%s start:%d end:%d length=%d CDS=%d-%d'%(t.strand,t.start,t.end,len(seq),
                                                              cds_start_transcript,
                                                              cds_end_transcript)
        transcriptRecord = SeqRecord(seq, id=t.id.replace('transcript:',''), description=desc)
        transcript_seq_list.append(transcriptRecord)
    else:
        it = [t.id.replace('transcript:',''), t.chrom, t.start, t.end,\
              cds_start_transcript, cds_end_transcript, t.strand, seq]
        transcript_seq_list.append(dict((_CSV_HEADER[i], it[i]) for i in range(len(_CSV_HEADER))))
    return transcript_seq_list

    
def get_transcript(args):
    '''
    parameters:
        args: parse from argparse
    return:
        elements write to a file or stdout
    '''
    db = gffutils.FeatureDB(args.database, keep_order=True) # load database
    feature_types = db.featuretypes()
    # assert GTF or GFF
    if args.rna_feature == 'mrna':
        mRNA_str = mRNA_type(args.style)
    else:
        mRNA_str = tuple(x for x in list(feature_types) if 'RNA' in x or 'transcript' in x)
    if not args.transcript:
        # loop all cdns in genome
        param_list = [(t, args.database, args.genome, args.style, args.upper, args.output_format) 
                     for t in db.features_of_type(mRNA_str, order_by='start')]
        with Pool(processes=args.process) as p:
            transcript_seq_list = list(tqdm(p.imap(sub_transcript, param_list), 
                                       total=len(param_list), ncols = 80, desc='Transcript processing:'))
        transcript_seq_list = [d for de in transcript_seq_list if de != None for d in de]
        parse_output(args, transcript_seq_list)
    else:
        for t in db.features_of_type(mRNA_str, order_by='start'):
            if args.transcript in t.id:
                param = (t, args.database, args.genome, args.style, args.upper, args.output_format)
                transcript_seq_list = sub_transcript(param)
                parse_output(args, transcript_seq_list)
                break 


# GenBank 基因组文件，是每条染色体一个LOCUS

def get_transcript_gb(args):
    '''
    '''
    transcript = []
    for record in create_db(args.genbank):
        for feature in record.features:
            if feature.type == 'exon': # CDS promoter UTR 
                transcript_seq = ''
                #for part in feature.location.parts:
                #    cds_seq += part.extract(record.seq)
                transcript_seq = feature.location.extract(record).seq
                # part.strand 会将FeatureLocation -1的反向互补
                # geneid or locus_tag 
                if 'locus_tag' in feature.qualifiers:
                    gene_id = feature.qualifiers['locus_tag'][0]
                elif 'gene' in feature.qualifiers:
                    gene_id = feature.qualifiers['gene'][0]
                else:
                    gene_id = "Null"
                # protein id  
                if 'protein_id' in feature.qualifiers:
                    protein_id = feature.qualifiers['protein_id'][0]
                else:
                    protein_id = 'Null'

                transcript_seq_record = SeqRecord(cds_seq,id='gene:%s protein:%s'%(gene_id, protein_id),
                                 description='strand %s length %d'%(feature.strand, len(cds_seq)))
                transcript.append(cds_seq_record)
                break 
        break     
    if args.print and args.format == 'dna':
        SeqIO.write(cds, sys.stdout, 'fasta')
    elif args.print and args.format == 'protein':
        SeqIO.write(proteins, sys.stdout, 'fasta')
    elif args.output and args.format == 'dna':
        SeqIO.write(cds, args.output, 'fasta')
    elif args.output and args.format == 'protein':
        SeqIO.write(proteins, args.output, 'fasta')
