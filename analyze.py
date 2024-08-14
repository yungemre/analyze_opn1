import subprocess
import os
from .analyze_paraphase import analyze_paraphase_output
from .table import table_header, write_table
from .snv import find_snv
from .combinations import analyze_combinations
from .LCR import find_LCR
from .save_json import save_as_json


def run_paraphase(paraphase, bam, reference, samtools, minimap2, sample_id, output):
    """
    Runs the paraphase tool.

    :param paraphase: Path to paraphase
    :param bam: Path to bam file
    :param reference: Path to reference genome
    :param samtools: Path to samtools
    :param minimap2: Path to minimap2
    :param sample_id: Sample ID
    :param output: Output directory
    :return json_output: Paraphase output file
    """

    # folder for paraphase output
    out_folder = f"{output}/{sample_id}_paraphase_output"
    os.mkdir(out_folder)

    # runs paraphase
    try:
        subprocess.run([paraphase, "-b", bam, "-g", "opn1lw", "-r", reference, "--samtools",
                        samtools, "--minimap2", minimap2, "-o", out_folder, "--prefix", f"{sample_id}"],
                       capture_output=True, text=True, check=True)

        print("Paraphase ran successfully.")
    except subprocess.CalledProcessError as e:
        print("Paraphase error: {e}")

    # path to json file
    json_output = f"{out_folder}/{sample_id}.paraphase.json"

    return json_output


def analyze(json_file, clair_file, sniffles_file, sample_id, output):
    """
    Analyzes the JSON output file generated by paraphase, a SNP vcf file (clair) and a structural vcf file (sniffles).

    :param json_file: JSON file generated by paraphase
    :param clair_file: SNP vcf file 
    :param sniffles_file: Structural vcf file
    :param sample_id: Sample ID
    :param output: Output directory
    """

    with open(f"{output}/{sample_id}_analysis.txt", 'w') as out_file:

        out_file.write(f"{sample_id} analysis summary\n\n")

        haplotype_list = analyze_paraphase_output(json_file, out_file)

        table = table_header()  # table to store possibly pathogenic variants

        table = find_LCR(sniffles_file, table)

        table = find_snv(clair_file, table)  # add possibly pathogenic SNV's to the table

        analyze_combinations(haplotype_list, table)

        write_table(out_file, table)

        save_as_json(table, sample_id, output)


def read_parameters(args):
    """
    Reads the command-line parameters and executes the corresponding function.

    :param args: Command-line arguments
    """

    # run paraphase
    if args.paraphase:
        json_file = run_paraphase(args.paraphase, args.bam, args.reference, args.samtools, args.minimap2, args.id, args.output)
        analyze(json_file, args.clair, args.sniffles, args.id, args.output)
    
    # analyze the files
    elif args.json:
        analyze(args.json, args.clair, args.sniffles, args.id, args.output)
