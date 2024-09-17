from .variants import Haer_Wigman_combinations
from .table import table_header


def get_entry_by_haplotype(haplotype):
    for entry in Haer_Wigman_combinations:
        if entry['haplotype'] == haplotype:
            return entry


def analyze_combinations(haplotype_list, table):
    # LIAVA combination
    if "opn1lw_LIAVA" in haplotype_list:

        hw_entry = get_entry_by_haplotype("opn1lw_LIAVA")
        hw_classification = hw_entry["Haer-Wigman_classification"]
        hw_disease = hw_entry['Haer-Wigman_disease']

        if "opn1mw_MVVVA" in haplotype_list:

            neitz_classification = "pathogenic in combination with opn1mw_MVVVA"
            neitz_disease = "protanopia"

        elif "opn1mw_MIAVA" in haplotype_list:

            neitz_classification = "pathogenic in combination with opn1mw_MIAVA"
            neitz_disease = "protanopia"

        else:
            neitz_classification = "pathogenic"
            neitz_disease = "BCM"

        table.append(["opn1lw_LIAVA", hw_classification, hw_disease, neitz_classification, neitz_disease])

    # opn1mw_LIAVA combination
    if "opn1mw_LIAVA" in haplotype_list and "opn1lw_LIAVA" not in haplotype_list:
        hw_classification = "/"
        hw_disease = "/"

        neitz_classification = "pathogenic"
        neitz_disease = "deuteranopia"

        table.append(["opn1lw_LIAVA", hw_classification, hw_disease, neitz_classification, neitz_disease])

    if "opn1lw_MIAVA" in haplotype_list:

        hw_entry = get_entry_by_haplotype("opn1lw_MIAVA")
        hw_classification = hw_entry['Haer-Wigman_classification']
        hw_disease = hw_entry['Haer-Wigman_disease']

        if haplotype_list.count("opn1lw_MIAVA") == 2:
            neitz_classification = "pathogenic in combination with second opn1lw_MIAVA"
            neitz_disease = "deuteranopia/myopia"

        else:
            neitz_classification = "/"
            neitz_disease = "/"

        table.append(["opn1lw_MIAVA", hw_classification, hw_disease, neitz_classification, neitz_disease])

    # opn1lw_LVAVA combinations
    if "opn1lw_LVAVA" in haplotype_list:

        hw_entry = get_entry_by_haplotype("opn1lw_LVAVA")
        hw_classification = hw_entry['Haer-Wigman_classification']
        hw_disease = hw_entry['Haer-Wigman_disease']

        if haplotype_list.count("opn1mw_LVAVA") == 2:
            neitz_classification = "pathogenic"
            neitz_disease = "deuteranopia"

        elif "opn1mw_LVAVA" in haplotype_list:

            neitz_classification = "normal in combination with opn1mw_LVAVA"
            neitz_disease = "/"

        elif "opn1lw_MVVVA" in haplotype_list:

            neitz_classification = "pathogenic in combination with opn1lw_MVVVA"
            neitz_disease = "deuteranopia"

        elif "opn1mw_MVVVA" in haplotype_list:

            neitz_classification = "normal in combination with opn1mw_MVVVA"
            neitz_disease = "/"

        elif "opn1lw_LVAIA" in haplotype_list:

            neitz_classification = "pathogenic in combination with opn1lw_LVAIA"
            neitz_disease = "deuteranopia"

        elif "opn1mw_LVAIA" in haplotype_list:

            neitz_classification = "normal in combination with opn1mw_LVAIA"
            neitz_disease = "/"

        elif "opn1mw_MVAVA" in haplotype_list:

            neitz_classification = "pathogenic in combination with opn1mw_MVAVA"
            neitz_disease = "severe myopia"

        else:
            neitz_classification = "pathogenic in combination with opn1lw_MIAVA"
            neitz_disease = "protanopia"

        table.append(["opn1lw_LVAVA", hw_classification, hw_disease, neitz_classification, neitz_disease])

    if "opn1mw_LVAVA" in haplotype_list:
        hw_entry = get_entry_by_haplotype("opn1mw_LVAVA")
        hw_classification = hw_entry['Haer-Wigman_classification']
        hw_disease = hw_entry['Haer-Wigman_disease']

        neitz_classification = "pathogenic"
        neitz_disease = "deuteranopia"

        table.append(["opn1mw_LVAVA", hw_classification, hw_disease, neitz_classification, neitz_disease])


    # list of pathogenic haplotypes (Haer-Wigman) that are not mentioned in Neit et al.
    hw_haplotypes = ["opn1lw_LIVVA", "opn1lw_MVAVA", "opn1mw_MIAVA", "opn1mw_MVAVA"]

    for haplotype in haplotype_list:

        # is haplotype pathogenic according to Haer-Wigman?
        if haplotype in hw_haplotypes:
            hw_entry = get_entry_by_haplotype(haplotype)

            hw_classification = hw_entry['Haer-Wigman_classification']
            hw_disease = hw_entry['Haer-Wigman_disease']

            neitz_classification = "/"
            neitz_disease = "/"

            table.append([haplotype, hw_classification, hw_disease, neitz_classification, neitz_disease])

    return table
