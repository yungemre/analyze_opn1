import argparse

def parameters():
    
    parser = argparse.ArgumentParser(description="Analyze paraphase output for pathogenic variants")

    parser.add_argument('-p', '--paraphase', nargs='?', const='paraphase', 
                        help='path to paraphase')
    parser.add_argument('-b', '--bam', 
                        help='bam file (required for paraphase)')
    parser.add_argument('-s', '--samtools', nargs='?', const='samtools', 
                        help='path to samtools (could be required for paraphase)')
    parser.add_argument('-m', '--minimap2', nargs='?', const='minimap2', 
                        help='path to minimap2 (could be required for paraphase)')
    parser.add_argument('-r', '--reference', 
                        help='path to reference genome fasta (e.g. GRCh38, required for paraphase)')
    parser.add_argument('-g', '--gene', required=True, 
                        help='gene name (supported genes: opn1lw)')
    parser.add_argument('-j', '--json', 
                        help='json file from paraphase output')
    parser.add_argument('-o', '--output', required=True, 
                        help='path for output')

    args = parser.parse_args() 

    return args