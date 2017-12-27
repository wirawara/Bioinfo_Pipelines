#!/bin/bash

echo Downloading GENCODE annotation

v=19

if [ ! -f gencode.v$v.annotation.gtf.gz ]
then
    wget ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_$v/gencode.v$v.annotation.gtf.gz
fi