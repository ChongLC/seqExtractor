#!/usr/bin/python

##########################################################################################
#                                       NOTE:                                            #
# This script extracts fasta sequence records from multiFASTA file based on a list of    # 
# record ids.                                                                            #
# Inspired by faSomeRecords and further improved by Li Chuin Chong and Yeo Keat Ee.      #
# Last updated: 1 Jan 2023                                                              #
##########################################################################################

import argparse
import time
import threading

def read_fasta(fasta_file):
    header_sequence = {}
    header = None
    sequence_lines = []
    
    with open(fasta_file) as file_content:
        for line in file_content:
            line = line.strip()
            if line.startswith(">"):
                if header is not None: 
                    header_sequence[header] = "".join(sequence_lines)
                header = line
                sequence_lines = []
            else: 
                sequence_lines.append(line)
        
        if header is not None: 
            header_sequence[header] = "".join(sequence_lines)
            
    return header_sequence

def write_result(output_filename, results):
  with open(output_filename, 'w') as fp:
      for id, seq in results.items():
          fp.write("%s\n" % id)
          fp.write("%s\n" % seq[0])
          fp.write("\n")

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

def process_record(record, target, matched, substring, method, case_insensitive, exclude):
    '''
    Process a single record and add it to the matched list 
    if its id is in the target list or its header contains the specified substring
    '''
    # mismatched.append(list(record))
    if method == 'id_list':              
        for i in target:
            if i in record[0]:
                matched[record[0]] = [record[1]]

    elif method == 'substring':
        if case_insensitive:
            if substring.lower() in record[0].lower(): 
                matched[record[0]] = [record[1]]
        else: 
            if substring in record[0]:
                matched[record[0]] = [record[1]]

def extractor(target_file, input_fasta_file, result_fasta_file, num_threads, method, substring=None, case_insensitive=False, exclude=False):
    '''
    Get the sequences that id matched with the id in the list or 
    header matched with the substring
    '''
    matched = {}
    if method == 'id_list': 
        target = generate_target(target_file)
    elif method == 'substring': 
        target = None
    input_objects = read_fasta(input_fasta_file)
    print('Input have {} sequences'.format(len(input_objects)))
    # Initialize a list to store the threads
    threads = []

    # Iterate over the record in the input file as dictionary 
    for record in input_objects.items():
        # Create a new thread to process this record
        thread = threading.Thread(target=process_record, args=(record, target, matched, substring, method, case_insensitive, exclude))
        thread.start()
        threads.append(thread)

        # If we have reached the maximum number of threads, wait for one to finish before starting a new one
        if len(threads) == num_threads:
            threads.pop().join()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    if exclude:
        mismatched = {k: [v] for k, v in input_objects.items() if k not in matched and v not in matched.values()}
        # Write the mismatched sequences to the result file
        print('Using exclude, output file has {} sequences.'.format(len(mismatched)))
        write_result(result_fasta_file, mismatched)
    else:
        print('Output file has {} matched sequences.'.format(len(matched)))
        # Write the matched sequences to the result file
        write_result(result_fasta_file, matched)

def parse_args():
    parser = argparse.ArgumentParser(
                        prog = 'seqExtractor.py',
                        description = 'Extract fasta sequence records from multiFASTA file based on a list of record ids or a substring in the sequence header'
                        )

    # Add the arguments
    parser.add_argument('-i', '--input', required=True, help='Filename include extension of original FASTA file')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--id_list', help='Filename include extension of the sequence ID list')
    group.add_argument('-s', '--substring', help='Substring to search for in the sequence header')
    parser.add_argument('-o', '--output', required=True, help='Filename include extension of output FASTA file')
    parser.add_argument('-t', '--threads', type=int, default=1, help='Number of threads to use (default: 1)')
    parser.add_argument('-c', '--case_insensitive', action='store_true', help='Make the substring search case insensitive (default: False)')
    parser.add_argument('-e', '--exclude', action="store_true", default=False, help="Option to exclude the sequences based on input ID list (default: False)")

    args = parser.parse_args()

    return args

def main():
    args=parse_args()
    input_file = args.input
    id_list_file = args.id_list
    output_file = args.output
    num_thread = args.threads
    substring = args.substring
    case_insensitive = args.case_insensitive
    exclude = args.exclude

    if substring: 
        method = 'substring'
    else: 
        method = 'id_list'
    extractor(id_list_file, input_file, output_file, num_thread, method, substring, case_insensitive, exclude)
    print("Done extracted!")

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %.2f time taken (s) ---" % (time.time() - start_time))
