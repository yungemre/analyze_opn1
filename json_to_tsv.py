import os
import json
import csv
import argparse

def process_json_files(input_folder, output_file):
    
    with open(output_file, 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(["Sample ID", "Sample Sex", "Possibly Pathogenic Variant", "Haer-Wigman Classification",
                         "Haer-Wigman Disease", "Neitz Classification", "Neitz Disease"])
              
        for filename in os.listdir(input_folder):
            if filename.endswith(".json"):
                filepath = os.path.join(input_folder, filename)
                          
                with open(filepath, 'r') as jsonfile:
                    data = json.load(jsonfile)                   
                    
                    for sample_id, entries in data.items():
					
                        if not entries: 
                            writer.writerow([sample_id, "", "None", "", "", "", ""])
							
                        else:
                            for entry in entries:
                                writer.writerow([
                                    sample_id,
                                    entry.get("sample_sex", ""),
                                    entry.get("variant", ""),
                                    entry.get("Haer_Wigman_classification", ""),
                                    entry.get("Haer_Wigman_disease", ""),
                                    entry.get("Neitz_classification", ""),
                                    entry.get("Neitz_disease", "")
                                ])
                        
                        writer.writerow([])

def main():
    
    parser = argparse.ArgumentParser(description='Process JSON files and convert them to a TSV file.')
    parser.add_argument('input_folder', type=str, help='Path to the folder containing JSON files')
    parser.add_argument('output_file', type=str, help='Path to the output TSV file')

    args = parser.parse_args()

    
    process_json_files(args.input_folder, args.output_file)

if __name__ == "__main__":
    main()
