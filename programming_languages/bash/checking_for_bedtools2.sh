#!/bin/bash

echo Checking for bedtools

# if file exists and there is a directory
if [ ! -d bedtools2 ]
then 
    git clone https://github.com/arq5x/bedtools2.git
    cd bedtools2
    make clean; make all
    cd ..
fi



