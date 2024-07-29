import argparse


def parameters():
    parser = argparse.ArgumentParser(description="Analyze paraphase output for pathogenic variants")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--paraphase', nargs='?', const='paraphase',
                       help='path to paraphase')
    group.add_argument('-j', '--json',
                       help='json file from paraphase output')

    parser.add_argument('-b', '--bam',
                        help='bam file (required for paraphase)')
    parser.add_argument('-c', '--clair', required=True,
                        help='clair file (vcf)')
    parser.add_argument('-f', '--sniffles', required=True,
                        help='sniffles file (vcf)')

    parser.add_argument('-s', '--samtools', nargs='?', const='samtools', default='samtools',
                        help='path to samtools (could be required for paraphase)')
    parser.add_argument('-m', '--minimap2', nargs='?', const='minimap2', default='minimap2',
                        help='path to minimap2 (could be required for paraphase)')
    parser.add_argument('-r', '--reference',
                        help='path to reference genome fasta (GRCh38, required for paraphase)')
    parser.add_argument('-o', '--output', required=True,
                        help='output directory')

    args = parser.parse_args()

    return args
