def write_copy_numbers(json_data, out_file):
    """
    Writes the copy numbers into the summary file.

    :param json_data: Paraphase results as dictionary
    :param out_file: txt file for analysis summary
    """

    out_file.write(f"Total copy number: {json_data['opn1lw']['total_cn']}\n")
    out_file.write(f"opn1lw copy number: {json_data['opn1lw']['opn1lw_cn']}\n")
    out_file.write(f"opn1mw copy number: {json_data['opn1lw']['opn1mw_cn']}\n\n")
    out_file.write("Annotated haplotypes:\n")


def extract_haplotypes(json_data, out_file):
    """
    Extracts the detected haplotypes from the paraphase results.

    :param data: Paraphase results as dictionary
    :param out_file: txt file for analysis summary
    :return: list of annotated haplotypes
    """

    haplotype_list = []

    for haplotype in json_data["opn1lw"]["annotated_haplotypes"]:

        current_haplotype = json_data["opn1lw"]["annotated_haplotypes"][haplotype]

        haplotype_list.append(current_haplotype)

        out_file.write(f"\t {current_haplotype} \n")

    out_file.write("\n")

    return haplotype_list

def analyze_paraphase_output(json_data, out_file):
    """
    Analyzes the paraphase results.

    :param json_file:
    :param out_file:
    :return: list of annotated haplotypes
    """

    write_copy_numbers(json_data, out_file)
    haplotype_list = extract_haplotypes(json_data, out_file)

    return haplotype_list
