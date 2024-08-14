def table_header():
    """
    Initializes the table for found variants and writes the header.

    :return: table with header
    """

    table = [
        ["Variant", "Haer-Wigman", "Neitz"],
        ["", "Classification", "Disease", "Classification", "Disease"]
    ]

    return table


def write_table(out_file, table):
    """
    Writes the given table into the output file

    :param out_file: txt file for analysis summary
    :param table: table with variants
    :return:
    """

    out_file.write("Possibly pathogenic variants:\n")
    
    if len(table) <= 2:
        out_file.write("None")
        print("finished")
    else:

        # Update to ensure all rows have the same number of columns by padding with empty strings
        max_columns = max(len(row) for row in table)
        for row in table:
            row.extend([""] * (max_columns - len(row)))

        # Calculate the maximum width for each column
        col_widths = [max(len(str(item)) for item in col) for col in zip(*table)]

        # Function to create the separator line
        def create_separator_line(col_widths):
            return "-" * (sum(col_widths) + 3 * (len(col_widths) - 1) + 4)

        # Write the table to a text file
        # Process the header row separately
        out_file.write(create_separator_line(col_widths) + "\n")
        header = table[0]
        header_line = (f"| {header[0].center(col_widths[0])} | {header[1].center(col_widths[1] + col_widths[2] + 3)} | "
                        f"{header[2].center(col_widths[3] + col_widths[4] + 3)} |")
        out_file.write(header_line + "\n")
        out_file.write(create_separator_line(col_widths) + "\n")

        # Process the rest of the table
        for row in table[1:]:
            line = " | ".join(str(item).center(col_widths[idx]) for idx, item in enumerate(row))
            out_file.write("| " + line + " |\n")
            out_file.write(create_separator_line(col_widths) + "\n")
            
        print("finished")
