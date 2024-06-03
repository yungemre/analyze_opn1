import subprocess
import json
from .opn1lw import opn1lw
from .smn1 import smn1


def run_paraphase(paraphase, bam, gene, reference, samtools, minimap2, output):
    """
    :param paraphase: path to paraphase
    :param bam: path to bam file
    :param gene: gene name (opn1lw)
    :param reference: path to reference genome
    :param samtools: path to samtools
    :param minimap2: path to minimap2
    :param output: output directory
    :return: /
    """

    # folder for paraphase output
    out_folder = output + "/paraphase_output"

    try:
        subprocess.run([paraphase, "-b", bam, "-g", gene, "-r", reference, "--samtools",
                        samtools, "--minimap2", minimap2, "-o", out_folder, "--prefix", gene],
                       capture_output=True, text=True, check=True)

        print("paraphase ran successfully")
    except subprocess.CalledProcessError as e:
        print("paraphase error: {e}")

    json_output = out_folder + '/' + gene + ".paraphase.json"

    analyze(json_output, gene, output)
    


def analyze(json_file, gene, output):
    """
    :param json_file: json file that was generated by paraphase
    :param gene: gene name (opn1lw)
    :param output: output directory
    :return: /
    """

    with open(json_file) as file:

        data = json.load(file)

        if gene == 'opn1lw':
            opn1lw(data, output) 
        elif gene == 'smn1':
            smn1(data, output)
        else:
            print(gene + " is not a supported gene.")
    

def read_parameters(args):
    """
    :param args:
    :return: /
    """

    if args.paraphase:
        run_paraphase(args.paraphase, args.bam, args.gene, args.reference, args.samtools, args.minimap2, args.output)
    elif args.json:
        analyze(args.json, args.gene, args.output)
