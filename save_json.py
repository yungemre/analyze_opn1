import json

def save_as_json(table, sample_id, output):

    variants_to_save = table[2:]

    variants = []

    for row in variants_to_save:
        variant = {
            "variant": row[0],
            "Haer_Wigman_classification": row[1],
            "Haer_Wigman_disease": row[2],
            "Neitz_classification": row[3],
            "Neitz_disease": row[4]
        }
        variants.append(variant)
        
    json_output = f"{output}/{sample_id}_variants.json"

    with open (json_output, "w") as json_file:
        json.dump({sample_id: variants}, json_file, indent=4)

