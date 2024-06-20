import json

def load_variants():
    """
    Loads the variant JSON file as a dictionary.

    :return: Variant dictionary
    """

    with open("bachelor/variants.json") as file:
        return json.load(file)

def write_copy_numbers(out_file, data):
    """
    Writes the copy numbers into the summary file.

    :param out_file: txt file for analysis summary
    :param data: Paraphase results as dictionary 
    """

    out_file.write(f"Total copy number: {data['opn1lw']['total_cn']}\n")
    out_file.write(f"opn1lw copy number: {data['opn1lw']['opn1lw_cn']}\n")
    out_file.write(f"opn1mw copy number: {data['opn1lw']['opn1mw_cn']}\n")
    out_file.write("Annotated haplotypes:\n")

def extract_haplotypes(data, lw_haplotype_list, mw_haplotype_list, out_file):
    """
    Extracts the detected haplotypes from the paraphase results.

    :param data: Paraphase results as dictionary
    :param lw_haplotype_list: List to store opn1lw haplotypes
    :param mw_haplotype_list: List to store opn1mw haplotypes
    :param out_file: txt file for analysis summary
    """

    for haplotype in data["opn1lw"]["annotated_haplotypes"]:
        haplotype_data = data["opn1lw"]["annotated_haplotypes"][haplotype].split('_')
        haplo_gene, variant = haplotype_data[0], haplotype_data[1]

        out_file.write(f"\t{haplo_gene}: {variant}\n")

        if haplo_gene == "opn1lw":
            lw_haplotype_list.append(variant)
        elif haplo_gene == "opn1mw":
            mw_haplotype_list.append(variant)

def check_variants(variants, haplotype_list):
    """
    Checks if the detected haplotypes are pathogenic.

    :param variants: Dictionary with opn1lw or opn1mw variants
    :param haplotype_list: List with detected haplotypes
    :return results: List of haplotypes that are possibly pathogenic
    """

    results = []
    for haplotype in variants["pathogenic"]:
        for detected_haplotype in haplotype_list:
            if haplotype == detected_haplotype:
                results.append(detected_haplotype)
    return results

def write_patho_variant(out_file, title, haplotypes):
    """
    Writes detected haplotypes that are possibly pathogenic into the summary file.

    :param out_file: txt file for analysis summary
    :param title: String that is written above the haplotypes
    :param haplotypes: List of haplotypes
    """
    
    if haplotypes:
        out_file.write(f"{title}\n")
        out_file.write('\t'.join(haplotypes) + '\n')

def opn1lw(data, output):
    """
    Analyzes opn1lw paraphase results.

    :param data: Paraphase results as dictionary
    :param output: Path for output file
    """
     
    lw_haplotype_list = []
    mw_haplotype_list = []

    variants = load_variants()

    with open(f"{output}/opn1lw_summary.txt", 'w') as out_file:
        write_copy_numbers(out_file, data)
        extract_haplotypes(data, lw_haplotype_list, mw_haplotype_list, out_file)
        out_file.write('\n')

        possible_patho_opn1lw = check_variants(variants["opn1lw"], lw_haplotype_list)
        write_patho_variant(out_file, "Following opn1lw variants are possibly pathogenic:", possible_patho_opn1lw)
        out_file.write('\n')

        # unknown_signif_opn1lw = check_variants(variants["opn1lw"], lw_haplotype_list, "unknown_significance")
        # write_patho_variant(out_file, "Following opn1lw variants have unknown significance:", unknown_signif_opn1lw)
        # out_file.write('\n')

        possible_patho_opn1mw = check_variants(variants["opn1mw"], mw_haplotype_list)
        write_patho_variant(out_file, "Following opn1mw variants are possibly pathogenic:", possible_patho_opn1mw)
        out_file.write('\n')

        # unknown_signif_opn1mw = check_variants(variants["opn1mw"], mw_haplotype_list, "unknown_significance")
        # write_patho_variant(out_file, "Following opn1mw variants have unknown significance:", unknown_signif_opn1mw)

    print("Finished: Results saved in summary file.")
