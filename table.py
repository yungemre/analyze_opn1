# Define the table structure with content, including merged cells in the header
table = [
    ["Variant", "Haer-Wigman", "Neitz"],
    ["", "Interpretation", "Disease", "Interpretation", "Disease"],
    ["c.607T>C p.(Cys203Arg)", "pathogenic", "unknown", "pathogenic", "BED"]
]

# Update to ensure all rows have the same number of columns by padding with empty strings
max_columns = max(len(row) for row in table)
for row in table:
    row.extend([""] * (max_columns - len(row)))

# Calculate the maximum width for each column
col_widths = [max(len(str(item)) for item in col) for col in zip(*table)]

# Path to save the text file
file_path = "table.txt"


# Function to create the separator line
def create_separator_line(col_widths):
    return "-" * (sum(col_widths) + 3 * (len(col_widths) - 1) + 4)


# Write the table to a text file
with open(file_path, "w") as file:
    # Process the header row separately
    header = table[0]
    header_line = f"| {header[0].center(col_widths[0])} | {header[1].center(col_widths[1] + col_widths[2] + 3)} | {header[2].center(col_widths[3] + col_widths[4] + 3)} |"
    file.write(header_line + "\n")
    file.write(create_separator_line(col_widths) + "\n")

    # Process the rest of the table
    for row in table[1:]:
        line = " | ".join(str(item).center(col_widths[idx]) for idx, item in enumerate(row))
        file.write("| " + line + " |\n")
        file.write(create_separator_line(col_widths) + "\n")
