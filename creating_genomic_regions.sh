#!/bin/bash

echo Creating exonic regions

v=19

if [ ! -f gencode_v${v}_exon_merged.bed.gz ]
then
    gunzip -c gencode.v$v.annotation.gtf.gz |
    awk 'BEGIN{OFS="\t";} $3="exon" {print $1,$4-1,$5}' |
    bedtools2/bin/sortBed |
    bedtools2/bin/mergeBed -i - | gzip > gencode_v${v}_exon_merged.bed.gz
fi    



echo Creating intronic regions

if [ ! -f gencode_v${v}_intron.bed.gz ]
then    
    gunzip -c gencode.v$v.annotation.gtf.gz |
    awk 'BEGIN{OFS="\t";} $3=="gene" {print $1,$4-1,$5}' |
    bedtools2/bin/sortBed |
    bedtools2/bin/subtractBed -a stdin -b gencode_v${v}_exon_merged.bed.gz |
    gzip > gencode_v${v}_intron.bed.gz
fi    



