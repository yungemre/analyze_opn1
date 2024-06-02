import subprocess
import json
from .opn1lw import opn1lw


def run_paraphase(paraphase, bam, gene, reference, samtools, minimap2, output):
    """
    :param paraphase:
    :param bam:
    :param gene:
    :param reference:
    :param samtools:
    :param minimap2:
    :param output:
    :return:
    """

    out_folder = output + "/paraphase"

    try:
        subprocess.run([paraphase, "-b", bam, "-g", gene, "-r", reference, "--samtools",
                        samtools, "--minimap2", minimap2, "-o", out_folder],
                       capture_output=True, text=True, check=True)

        print("paraphase ran successfully")
    except subprocess.CalledProcessError as e:
        print("paraphase error: {e}")


def analyze_json(json_file, gene, output):
    """
    :param json_file:
    :param gene:
    :param output:
    :return:
    """

    with open(json_file) as file:

        data = json.load(file)

        if gene == 'opn1lw':
            opn1lw(data, output) 
        else:
            print(gene + " is not a supported gene.")
    

def read_parameters(args):
    """
    :param args:
    :return:
    """

    if args.paraphase:
        run_paraphase(args.paraphase, args.bam, args.gene, args.reference, args.samtools, args.minimap2, args.output)

    if args.json:
        analyze_json(args.json, args.gene, args.output)
