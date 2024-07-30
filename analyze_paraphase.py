import json


def write_copy_numbers(data, out_file):
    """
    Writes the copy numbers into the summary file.

    :param data: Paraphase results as dictionary
    :param out_file: txt file for analysis summary
    """

    out_file.write(f"Total copy number: {data['opn1lw']['total_cn']}\n")
    out_file.write(f"opn1lw copy number: {data['opn1lw']['opn1lw_cn']}\n")
    out_file.write(f"opn1mw copy number: {data['opn1lw']['opn1mw_cn']}\n\n")
    out_file.write("Annotated haplotypes:\n")


def extract_haplotypes(data, out_file):
    """
    Extracts the detected haplotypes from the paraphase results.

    :param data: Paraphase results as dictionary
    :param out_file: txt file for analysis summary
    :return: list of annotated haplotypes
    """

    haplotype_list = []

    for haplotype in data["opn1lw"]["annotated_haplotypes"]:

        current_haplotype = data["opn1lw"]["annotated_haplotypes"][haplotype]

        haplotype_list.append(current_haplotype)

        out_file.write(f"\t {current_haplotype} \n")

    out_file.write("\n")

    return haplotype_list

def analyze_paraphase_output(json_file, out_file):
    """
    Analyzes the paraphase results.

    :param json_file:
    :param out_file:
    :return: list of annotated haplotypes
    """

    with open(json_file) as file:
        data = json.load(file)

    write_copy_numbers(data, out_file)
    haplotype_list = extract_haplotypes(data, out_file)

    return haplotype_list
