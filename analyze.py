import subprocess
import json
from .opn1lw import opn1lw
from .analyze_paraphase import analyze_paraphase_output
from .table import table_header, write_table
from .snv import find_snv


def run_paraphase(paraphase, bam, reference, samtools, minimap2, output):
    """
    Runs the paraphase tool.

    :param paraphase: Path to paraphase
    :param bam: Path to bam file
    :param reference: Path to reference genome
    :param samtools: Path to samtools
    :param minimap2: Path to minimap2
    :param output: Output directory
    :return json_output: paraphase output file
    """

    # folder for paraphase output
    out_folder = f"{output}/paraphase_output"

    try:
        subprocess.run([paraphase, "-b", bam, "-g", "opn1lw", "-r", reference, "--samtools",
                        samtools, "--minimap2", minimap2, "-o", out_folder, "--prefix", "gene", "opn1lw"],
                       capture_output=True, text=True, check=True)

        print("Paraphase ran successfully.")
    except subprocess.CalledProcessError as e:
        print("Paraphase error: {e}")

    json_output = f"{out_folder}/opn1lw.paraphase.json"

    return json_output


def analyze(json_file, clair_file, sniffles_file, output):
    """
    Analyzes the JSON output file generated by paraphase.

    :param json_file: JSON file generated by paraphase
    :param output: Output directory
    """

    with open(f"{output}/analysis_summary.txt", 'w') as out_file:

        haplotype_list = analyze_paraphase_output(json_file, out_file)

        table = table_header() # table to store possbily pathogenic variants

        table = find_snv(clair_file, table) # add possibly pathogenic SNV's to the table

        write_table(out_file, table)




def read_parameters(args):
    """
    Reads the command-line parameters and executes the corresponding function.

    :param args: Command-line arguments
    """

    if args.paraphase:
        json_file = run_paraphase(args.paraphase, args.bam, args.reference, args.samtools, args.minimap2, args.output)
        analyze(json_file, args.clair, args.sniffles, args.output)
    elif args.json:
        analyze(args.json, args.clair, args.sniffles, args.output)
