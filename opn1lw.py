
def opn1lw(data, output):

    # write the output file
    with open(output + "/opn1lw_summary.txt", 'w') as out_file:

        out_file.write("Total copy number: " + str(data["opn1lw"]["total_cn"]) + '\n')

        out_file.write("opn1lw copy number: " + str(data["opn1lw"]["opn1lw_cn"]) + '\n')

        out_file.write("opn1mw copy number: " + str(data["opn1lw"]["opn1mw_cn"]) + '\n')

        out_file.write("Annotated haplotypes: " + '\n')

        # lists to store haplotypes
        lw_haplotype_list = []
        mw_haplotype_list = []

        for haplotype in data["opn1lw"]["annotated_haplotypes"]:

            haplotype = data["opn1lw"]["annotated_haplotypes"][haplotype].split('_')

            # write annotated haplotype into the summary file
            out_file.write('\t' + haplotype[0] + ": " + haplotype[1] + '\n')

            # add haplotype to the list
            if "opn1lw" == haplotype[0]:
                lw_haplotype_list.append(haplotype[1])
            elif "opn1mw" == haplotype[0]:
                mw_haplotype_list.append(haplotype[1])

        
        # are the haplotypes pathogenic?

        

