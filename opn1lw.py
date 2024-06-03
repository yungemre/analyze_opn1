import json

def opn1lw(data, output):
    """
    :param data:
    :param output:
    :return:
    """

    # lists to store haplotypes
    lw_haplotype_list = []
    mw_haplotype_list = []

    possible_patho_opn1lw = []
    possible_patho_opn1mw = []

    unknown_signif_opn1lw = []
    unknown_signif_opn1mw = []


    # opn1lw/opn1mw variants
    with open("bachelor/variants.json") as variants_file:
        variants = json.load(variants_file)

        # write the output file
        with open(output + "/opn1lw_summary.txt", 'w') as out_file:

            out_file.write("Total copy number: " + str(data["opn1lw"]["total_cn"]) + '\n')

            out_file.write("opn1lw copy number: " + str(data["opn1lw"]["opn1lw_cn"]) + '\n')

            out_file.write("opn1mw copy number: " + str(data["opn1lw"]["opn1mw_cn"]) + '\n')

            out_file.write("Annotated haplotypes: " + '\n')


            for haplotype in data["opn1lw"]["annotated_haplotypes"]:

                haplotype = data["opn1lw"]["annotated_haplotypes"][haplotype].split('_')

                # write annotated haplotype into the summary file
                out_file.write('\t' + haplotype[0] + ": " + haplotype[1] + '\n')

                # add haplotype to the list
                if "opn1lw" == haplotype[0]:
                    lw_haplotype_list.append(haplotype[1])
                elif "opn1mw" == haplotype[0]:
                    mw_haplotype_list.append(haplotype[1])

            out_file.write('\n')

            # are the opn1lw haplotypes pathogenic?
            for haplotype in variants["opn1lw"]["pathogenic"]:
                for detected_haplotype in lw_haplotype_list:
                    if haplotype == detected_haplotype:
                        possible_patho_opn1lw.append(detected_haplotype)
                
            out_file.write("Following opn1lw variants are possibly pathogenic:" + '\n')

            if not possible_patho_opn1lw:
                out_file.write("None")
            else:
                for h in possible_patho_opn1lw:
                    out_file.write(h + '\t')

            out_file.write('\n')

            # unknown siginificance opn1lw
            for haplotype in variants["opn1lw"]["unknown_significance"]:
                for detected_haplotype in lw_haplotype_list:
                    if haplotype == detected_haplotype:
                        unknown_signif_opn1lw.append(detected_haplotype)

            if unknown_signif_opn1lw:
                out_file.write("Following opn1lw variants have unknown significance:" + '\n')
                for h in unknown_signif_opn1lw:
                    out_file.write(h + '\t')

            out_file.write('\n')
            out_file.write('\n')

            # are the opn1mw haplotypes pathogenic?
            for haplotype in variants["opn1mw"]["pathogenic"]:
                for detected_haplotype in mw_haplotype_list:
                    if haplotype == detected_haplotype:
                        possible_patho_opn1mw.append(detected_haplotype)

            out_file.write("Following opn1mw variants are possibly pathogenic:" + '\n')

            if not possible_patho_opn1mw:
                out_file.write("None")
            else:
                for h in possible_patho_opn1mw:
                    out_file.write(h + '\t')

            out_file.write('\n')

            # unknown siginificance opn1mw
            for haplotype in variants["opn1mw"]["unknown_significance"]:
                for detected_haplotype in mw_haplotype_list:
                    if haplotype == detected_haplotype:
                        unknown_signif_opn1mw.append(detected_haplotype)

            if unknown_signif_opn1mw:
                out_file.write("Following opn1mw variants have unknown significance:" + '\n')
                for h in unknown_signif_opn1mw:
                    out_file.write(h + '\t')

    print("Finished: Results saved in summary file.")


