# -*- coding: utf-8 -*-
import sys
import gffutils
import pandas as pd 
from tqdm import tqdm 
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from multiprocessing import Pool
from collections import defaultdict, deque
from featurExtract.commands.extract_uorf import GFF
from featurExtract.utils.util import utr3_type, utr5_type, mRNA_type
from featurExtract.utils.util import stop_codon_seq, add_stop_codon, parse_output
from featurExtract.utils.visualize import visual_transcript, visual_transcript_genome

# table header 
_dORF_csv_header = ['TranscriptID', 'Chrom', 'Strand', \
                    'CDS Interval', 'dORF Start', 'dORF End', \
                    'dORF Type', 'dORF Length', 'dORF']



class dORF(object):
    """dORF finder using object-oriented
    Attributes:
        transcript_id (str): transcript id
        chorm (str): chromosome id 
        strand (str): transcript strand 
        matural_transcript (Seq of Biopython): matural transcript sequence
        coding_sequence (Seq of Biopython): conding sequence of specifity transcript 
    """
    START_CODON = 'ATG'
    STOP_CODON_LIST = ['TAA','TAG','TGA']
    
    def __init__(self, transcript_id, length, chrom, strand, matural_transcript, coding_sequence):
        self.t_id = transcript_id
        self.length = length
        self.chrom = chrom
        self.strand = strand 
        self.mt = matural_transcript
        self.cds = coding_sequence
    def transcript_location(self):
        """Transcript start and end
        1D list regradless of strand  
        """
        return [0,len(self.mt)]
    def cds_location_transcript(self):
        """Extract the cds start and end in transcript
        1D list regardless of strand 
        """
        start_codon_position = self.mt.index(self.cds)
        cds_start = start_codon_position + 1
        cds_end = start_codon_position + len(self.cds)
        return [cds_start, cds_end]

    def dorf_location_transcript(self):
        """Extract dorfs start and end in transcript
        2D list regardless strand 
        """
        d2 = []
        dORF_dict = self.dorf_parse()
        for dorf_type in dORF_dict.keys():
            for it in dORF_dict[dorf_type]:
                if len(it[8]) <= self.length:
                    continue
                dorf_start, dorf_end = it[4], it[5]
                d2.append([dorf_start, dorf_end])
        return d2
    def dorf_parse(self):
        """ dORF parse"""
        dORF_dict = defaultdict(list)
        # start_codon means the first base position in matural_transcript
        start_codon = self.mt.index(self.cds)
        # stop_codon means the last base position in matural transcript
        cds_len = len(self.cds)
        stop_codon = start_codon + cds_len
        cds_intervel = str(start_codon) + '-' + str(stop_codon)
        mt_len = len(self.mt)
        utr5 = self.mt[:start_codon]
        utr5_len = len(utr5)
        utr3 = self.mt[stop_codon:]
        utr3_len = len(utr3)
        for i in range(0, utr3_len-3):
            # start codon find 
            if utr3[i:i+3] == dORF.START_CODON:
                for j in range(i+3, utr3_len, 3):
                # stop codon find
                    if utr3[j:j+3] in dORF.STOP_CODON_LIST:
                        dorf = utr3[i:j+3]
                        out1 = [self.t_id, self.chrom, self.strand, cds_intervel, stop_codon+i+1, stop_codon+j+3, 'dORF', len(dorf), dorf]
                        if not dORF_dict.get('dORF'):
                            dORF_dict['dORF'] = [out1]
                        else:
                            dORF_dict['dORF'].append(out1)
                        break
        return dORF_dict
     
def dorf_procedure_oriented(transcript_id, chrom, strand, matural_transcript, coding_sequence):
    """
    Parameters:
        transcript_id:      transcript id
        matural_transcript: a Seq type (Biopython) from mature transcript without intron
        coding_sequence:    a Seq type (Biopython) from coding sequence start with ATG , 
                         end with TAA, TGA, TAG
    Return:
        down stream open reading frame in utr3
    """
    dORF_dict = defaultdict(list)
    stop_codon_list = ['TAA','TAG','TGA']
    # start_codon means the first base position in matural_transcript
    start_codon = matural_transcript.index(coding_sequence)
    # stop_codon means the last base position in matural transcript
    cds_len = len(coding_sequence)
    stop_codon = start_codon + cds_len
    cds_intervel = str(start_codon) + '-' + str(stop_codon)
    mt_len = len(matural_transcript)
    utr5 = matural_transcript[:start_codon]
    utr5_len = len(utr5)
    utr3 = matural_transcript[stop_codon:]
    utr3_len = len(utr3)
    for i in range(0, utr3_len-3):
        # start codon find 
        if utr3[i:i+3] == "ATG":
            for j in range(i+3, utr3_len, 3):
            # stop codon find
                if utr3[j:j+3] in stop_codon_list:
                    dORF = utr3[i:j+3]
                    out1 = [transcript_id, chrom, strand, cds_intervel, stop_codon+i+1, stop_codon+j+3, 'dORF', len(dORF), dORF]
                    if not dORF_dict.get('dORF'):
                        dORF_dict['dORF'] = [out1]
                    else:
                        dORF_dict['dORF'].append(out1)
                    break 
    return dORF_dict



def get_mt_cds_seq(t, db, genome, style):
    """
    parameters:
        args:  
    """
    # primary transcript (pt) 是基因组上的转录本的序列，
    # 有的会包括intron，所以提取的序列和matural transcript (mt) 不一致
    # pt = t.sequence(genome, use_strand=True)
    # matural transcript (mt)
    # 该步骤是获取序列: 转录本序列，CDS序列, five_prime_UTR, three_prime_UTR
    # 但是有的基因注释不正确，导致成熟转录本序列的两个来源不一致，一个是exon来源的，一个是five_prime_UTR和CDS来源的
    # 针对这种请情况，我们使用 five_prime_UTR + CDS + three_prime_UTR 拼接形成成熟的转录本序列用于uORF/dORF的注释
    # exon 提取的是转录本内成熟的mRNA的序列,即外显子按基因组坐标首尾相连的matural transcript
    mt, cds = '', ''
    exons_list = []
    for e in db.children(t, featuretype='exon', order_by='start'):
        exons_list.append((e.start, e.end))
        mt += e.sequence(genome, use_strand=False) # 不反向互补，对于负链要得到全部的cds后再一次性反向互补
    mt = Seq(mt)
    if t.strand == '-':
        mt = mt.reverse_complement()
    # CDS 提取的是编码区 ATG ... TAG
    cds_list = []
    for c in db.children(t, featuretype='CDS', order_by='start'):
        cds_list.append((c.start, c.end))
        cds += c.sequence(genome, use_strand=False) # 不反向互补，对于负链要得到全部的cds后再一次性反向互补
    if style == 'GTF':
        sc_seq = stop_codon_seq(db, t, genome)
        cds = add_stop_codon(cds, t.strand, sc_seq)
    cds = Seq(cds)
    ## 需要确定exon和mRNA的位置是否一致，不一致以mRNA为准
    # mt from utr5/3 and cds
    mt_from_utr_cds = ''
    for e in db.children(t, featuretype=['five_prime_UTR', 'CDS', 'three_prime_UTR'], order_by='start'):
        mt_from_utr_cds += e.sequence(genome, use_strand=False)
    mt_from_utr_cds = Seq(mt_from_utr_cds)
    if t.strand == '-':
        mt_from_utr_cds = mt_from_utr_cds.reverse_complement()
    if mt != mt_from_utr_cds:
        mt = mt_from_utr_cds
        # error_count += 1
    if t.strand == '-':
        cds = cds.reverse_complement()
    return mt, cds, exons_list, cds_list


def dorf_filter_output(params):
    t, database, genome, style, length, output_format = params
    db = gffutils.FeatureDB(database, keep_order=True)
    index = 0
    dORF_seq_list = deque()
    # 可以多进程,但是多进程会导致和SQLite数据库的交互产生错误
    mt, cds, exons_list, cds_list = get_mt_cds_seq(t, db, genome, style)
    # objected-oriented
    if mt == cds: # not contain dORF
        return
    if len(cds) % 3 != 0: # CDS error
        return
    dORF_ = dORF(t.id, length, t.chrom, t.strand, mt, cds)
    dORF_dict = dORF_.dorf_parse()
    if len(dORF_dict) == 0: # CDS error
        return
    # loop for type1, type2 and type3
    for key in sorted(dORF_dict.keys()):
        # print(key,len(dORF_dict[key]))
        for it in dORF_dict[key]:
            # dORF length filter 
            if len(it[8]) <= length:
                # default: 6
                continue
            # csv output format 
            if output_format == 'fasta':
                uorf_id = ".".join(map(str,[it[0], it[4], it[5], it[6]]))
                seq = it[8] # it[8] is s Seq type
                desc='strand:%s dORF=%d-%d %s length=%d CDS=%s-%s'%(it[2],
                                                              it[4],
                                                              it[5],
                                                              it[6],
                                                              len(seq),
                                                              it[3].split('-')[0],
                                                              it[3].split('-')[1])
                uorfRecord = SeqRecord(seq, id=uorf_id.replace('transcript:',''), description=desc)
                dORF_seq_list.append(uorfRecord)

            elif output_format == 'gff':
                gff = GFF(exons_list, it, 'dORF')
                uorf_gff_line,features_gff_lines = gff.parse()
                # print(uorf_gff_line)
                # dORF_gff.write(uorf_gff_line+"\n")
                dORF_seq_list.append(uorf_gff_line)
                for feature_line in features_gff_lines:
                    # print(feature_line)
                    dORF_seq_list.append(feature_line)
                    # dORF_gff.write(feature_line+"\n")
            else:
                # csv output_format
                dORF_seq_list.append(dict(zip(_dORF_csv_header, it)))
                index += 1
    return dORF_seq_list


def get_dorf(args):
    """
    parameters:
        args: parse from argparse
    return:
        elements write to a file or stdout 
    """
    db = gffutils.FeatureDB(args.database, keep_order=True) # load database
    feature_types = db.featuretypes()
    if args.rna_feature == 'mrna':
        mRNA_str = mRNA_type(args.style)
    else:
        mRNA_str = tuple(x for x in list(feature_types) if 'RNA' in x or 'transcript' in x)
    error_count = 0
    total_transcript_number = len(list(db.features_of_type(mRNA_str, order_by='start')))
    # loop all transcripts in genome
    if not args.transcript:
        param_list = [(t, args.database, args.genome, args.style, args.length, args.output_format) for t in db.features_of_type(mRNA_str, order_by='start')]
        with Pool(processes=args.process) as p:
            dORF_seq_list = list(tqdm(p.imap(dorf_filter_output, param_list), total=len(param_list), ncols = 80, desc='dORF processing:'))
        dORF_seq_list = [d for de in dORF_seq_list if de != None for d in de]
        # output file 
        parse_output(args, dORF_seq_list)
    else:
        # specify the transcript id; only one transcript
        for t in db.features_of_type(mRNA_str, order_by='start'):
            # primary transcript (pt) 是基因组上的转录本的序列，
            # 有的会包括intron，所以提取的序列和matural transcript 不一致
            # id specify
            if args.transcript in t.id:
                params = (t, args.database, args.genome, args.style, args.length, args.output_format)
                dORF_seq_list = dorf_filter_output(params)
                mt, cds, exons_list, cds_list = get_mt_cds_seq(t, db, args.genome, args.style)
                dORF_ = dORF(t.id, args.length, t.chrom, t.strand, mt, cds)
                dORF_dict = dORF_.dorf_parse()
                dorf_location_genome = [] # for schematic on genome # 3D list 
                for key in sorted(dORF_dict.keys()):
                    for it in dORF_dict[key]:
                        # dORF length filter 
                        if len(it[8]) <= args.length:
                            # default: 6
                            continue
                        # for schematic on genome
                        gff = GFF(exons_list, it, 'dORF')
                        ex_locations = gff.uorf_exons_location()
                        dorf_location_genome.append(ex_locations)
                # figure the schametic 
                # without intron / -m 
                if args.schematic_without_intron:
                    figure = visual_transcript(args.schematic_without_intron,
                                               args.transcript,
                                               dORF_.transcript_location(),
                                               dORF_.cds_location_transcript(),
                                               dORF_.dorf_location_transcript(),
                                               'dORF')
                    figure.draw()
                # with intron / -n 
                if args.schematic_with_intron:
                    figure = visual_transcript_genome(t.strand,
                                                      args.schematic_with_intron,
                                                      args.transcript,
                                                      exons_list,
                                                      cds_list,
                                                      dorf_location_genome,# 3D list 
                                                      'dORF')
                    figure.draw()
                # file out
                parse_output(args, dORF_seq_list)
                break
