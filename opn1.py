import gzip
import pysam

found_variants = {SNV: [], LCR: True, combinations: []}

def SNV():

    file = "/mnt/storage3b/projects/research/23014I_1145_ONTpilot_TNAMSE/Sample_23014LRa023L2_01/clair_temp/full_alignment.vcf.gz"

    snv = {('chrX', 154154602, 'T', 'C')}  # more SNVs can be added

    with gzip.open(file, 'rt') as vcf:
        vcf_reader = vcf_Reader(vcf)

        for record in vcf_reader:
            key = (record.CHROM, record.POS, record.REF, str(record.ALT[0]))

            print(key)

# def opn1(json_file, clair_file, sniffles_file, output):

