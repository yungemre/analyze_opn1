from pysam import VariantFile


def find_LCR(file, table):
    # LCR coordinates
    chromosome = "chrX"
    start_position = 154118184
    end_position = 154191311

    vcf_file = VariantFile(file)

    # search for deletion
    for record in vcf_file.fetch(chromosome, start_position, end_position):
        if 'SVTYPE' in record.info and record.info['SVTYPE'] == 'DEL':
            variant_start = record.pos
            variant_end = record.stop

            if variant_start == start_position and variant_end == end_position:
                print("LCR deletion found")

                table.append(["Missing LCR", "pathogenic", "BCM", "pathogenic", "BCM"])

    return table
