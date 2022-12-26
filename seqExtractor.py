#!/usr/bin/python

##########################################################################################
#                                       NOTE:                                            #
# This script extracts fasta sequence records from multiFASTA file based on a list of    # 
# record ids.                                                                            #
# Inspired by faSomeRecords and further improved by Li Chuin Chong and Yeo Keat Ee.      #
# Last updated: 26 Dec 2022                                                              #
##########################################################################################

from Bio import SeqIO
import argparse
import time
import threading

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

def process_record(record, target, matched):
    '''
    Process a single record and add it to the matched list if its id is in the target list
    '''
    for i in target:
        if i in record.description:
            matched.append(record)
            break

def extractor(target_file, input_fasta_file, result_fasta_file, num_threads):
    '''
    Get the sequences that id matched with the id in list
    '''
    matched = []
    target = generate_target(target_file)
    input_objects = SeqIO.parse(input_fasta_file, "fasta")
    # Initialize a list to store the threads
    threads = []
    # Iterate over the records in the input file
    for record in input_objects:
        # Create a new thread to process this record
        thread = threading.Thread(target=process_record, args=(record, target, matched))
        thread.start()
        threads.append(thread)

        # If we have reached the maximum number of threads, wait for one to finish before starting a new one
        if len(threads) == num_threads:
            threads.pop().join()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    # Write the matched sequences to the result file
    SeqIO.write(matched, result_fasta_file, "fasta")

def parse_args():
    parser = argparse.ArgumentParser(
                        prog = 'seqExtractor.py',
                        description = 'Extract fasta sequence records from multiFASTA file based on a list of record ids'
                        )

    # Add the arguments
    parser.add_argument('-i', '--input', required=True, help='Filename include extension of original FASTA file')
    parser.add_argument('-l', '--id_list', required=True, help='Filename include extension of the sequence ID list')
    parser.add_argument('-o', '--output', required=True, help='Filename include extension of output FASTA file')
    parser.add_argument('-t', '--threads', type=int, default=1, help='Number of threads to use (default: 1)')

    args = parser.parse_args()

    return args

def main():
    args=parse_args()
    input_file = args.input
    id_list_file = args.id_list
    output_file = args.output
    num_thread = args.threads
    extractor(id_list_file, input_file, output_file, num_thread)
    print("Done extracted!")

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %.2f time taken (s) ---" % (time.time() - start_time))