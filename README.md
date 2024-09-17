# Analyze the OPN1LW/OPN1MW gene cluster
Detection of pathogenic variants in the OPN1LW/OPN1MW gene cluster using long reads.

# Usage

## Run with Paraphase

```
python -m analyze_opn1 -p \
-b mapping.bam -c SNV.vcf.gz -f structurals_variants.vcf.gz \
-i sample_id -o output_directory \
-r reference.fa
```

## Run without Paraphase

```
python -m analyze_opn1 -j paraphase.json \
-c SNV.vcf.gz -f structurals_variants.vcf.gz \
-i sample_id -o output_directory
```

## Parameters

| Parameter | Description|
|:------------|:-----------|
| -p, --paraphase | required to run paraphase |
| -j, --json   | json paraphase output if paraphase already was executed |
| -b, --bam    | required to run paraphase |
| -c, --clair | required SNV vcf file |
| -f, --sniffles | required structural variant file |
| -i, --id | required sample id |
| -r, --reference | required to run paraphase (fasta) |
| -o, --output | required path to output directory |
| -s, --samtools | optional path to samtools (for paraphase) |
| -m, --minimap2 | optional path to minimap2 (for paraphase) |
