#! /usr/bin/env python

import argparse


"""
usage: python fasta_to_fastq.py -in INPUT (fasta) -out OUTPUT -q [-q QUALITY SCORE]

To make the fastA file into a fastQ file, we need to make 4 rows for each “>” in the fastA file.

1 .the name from the “>” line in fastA, just starting with “@” instead of “>”
2. sequence (unfolded version of sequence in fastA)
3. +
4.  quality scores that we have to make up because they don’t exist in fastA 

"""

def run(args):
	qual = args.quality_score
	f = open(args.input)
	fout = open(args.output, "w")
	seq = ""
	for line in f:
		if line[0] == ">":
			if seq != "":
				fout.write(seq + "\n")
				fout.write("+\n")
				fout.write(qual * len(seq) + "\n")
			fout.write("@" + line[1:])
			seq = ""
		else:
			seq += line.strip()
	f.close()

	fout.write(seq + "\n")
	fout.write("+\n")
	fout.write(qual * len(seq) + "\n")
	fout.close()


def main():
    parser=argparse.ArgumentParser(description="Convert a fastA file to a FastQ file")
    parser.add_argument("-in",help="fasta input file", dest="input", type=str, required=True)
    parser.add_argument("-out",help="fastq output filename",dest="output", type=str, required=True)
    parser.add_argument("-q",
    help="Quality score to fill in (since fasta doesn't have quality scores but fastq needs them. Default=I" ,
    dest="quality_score", type=str, default="I")
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()
  