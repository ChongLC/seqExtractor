#!/usr/bin/python

##########################################################################################
#                                       NOTE:                                            #
# This script extracts fasta sequence records from multiFASTA file based on a list of    # 
# record ids.                                                                            #
# Inspired by faSomeRecords and further improved by Li Chuin Chong and Yeo Keat Ee.      #
# Last updated: 24 Dec 2022                                                              #
##########################################################################################

from Bio import SeqIO
import argparse
import time

def generate_target(target_file):
    '''
    Get the unique target id list from target file
    '''
    wanted = set()
    with open(target_file) as f:
        for line in f:
            line = line.strip()
            if line != "":
                wanted.add(line)
    return list(wanted)


def extractor(target_file, input_fasta_file, result_fasta_file):
    '''
    Get the sequences that id matched with the id in list
    '''
    matched = []
    target = generate_target(target_file)
    input_objects = SeqIO.parse(input_fasta_file, "fasta")
    for record in input_objects:
      for i in target:
        if i in record.description:
          matched.append(record)
    
    # write a complete set of SeqRecord objects into the result file
    SeqIO.write(matched, result_fasta_file, "fasta")

def parse_args():
    parser = argparse.ArgumentParser(
                        prog = 'seqExtractor',
                        description = 'Extract fasta sequence records from multiFASTA file based on a list of record ids'
                        )

    # Add the arguments
    parser.add_argument('-f', '--fasta', required=True, help='Filename include extension of original FASTA file')
    parser.add_argument('-l', '--id_list', required=True, help='Filename include extension of the sequence ID list')
    parser.add_argument('-r', '--result', help='Filename include extension of output FASTA file')
    -e, --exclude

    args = parser.parse_args()

    return args

def main():
    inputs=parse_args()
    input_file = inputs.fasta
    wanted_file = inputs.wanted
    result_file = inputs.result
    extractor(wanted_file, input_file, result_file)
    print("Done extracted!")

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %.2f time taken (s) ---" % (time.time() - start_time))