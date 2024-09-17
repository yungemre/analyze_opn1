# Analyze the OPN1LW/OPN1MW gene cluster
Analysis of genetic variants in duplicate genes using long Nanopore reads

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
