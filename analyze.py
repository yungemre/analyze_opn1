
import json
from .opn1lw import opn1lw


def run_paraphase(paraphase, bam, gene, reference, samtools, minimap2):
    print("TODO run paraphase")


def analyze_json(json_file, gene, output):

    with open(json_file) as file:

        data = json.load(file)

        if gene == 'opn1lw':
            opn1lw(data, output) 
        else:
            print(gene + " is not a supported gene.")   

        file.close()
    

def read_parameters(args):

    if args.paraphase:
        run_paraphase(args.paraphase, args.bam, args.gene, 
                      args.reference, args.samtools, args.minimap2)

    if args.json:
        analyze_json(args.json, args.gene, args.output)