from pysam import VariantFile


def find_LCR(file, table):
    # LCR coordinates
    chromosome = 'X'
    start_position = 154118184
    end_position = 154191311

    vcf_file = VariantFile(file)

    # search for deletion
    deletion_found = False
    for record in vcf_file.fetch(chromosome, start_position, end_position):
        if 'SVTYPE' in record.info and record.info['SVTYPE'] == 'DEL':
            print("LCR deletion found")
            deletion_found = True

        table.append(["Missing LCR", "pathogenic", "BCM", "pathogenic", "BCM"])

    return table
