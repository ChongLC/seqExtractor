# seqExtractor
A python tool to extract multiple fasta sequence records from multiFASTA file based on a list of record ids or a substring in the sequence header. <br>
Written by: [Li Chuin Chong](https://github.com/ChongLC) and [Yeo Keat Ee](https://github.com/ee2110)

---

## Installation
1. Download only the python code <br>
    ```
    wget https://raw.githubusercontent.com/ChongLC/seqExtractor/master/seqExtractor.py
    ```

2. Download the entire repo


To use the `seqExtractor`, the following packages are needed to be installed: 
- Biopython
- argparse

You can install these packages using `pip`: 
```
pip install biopython argparse
```

---

## Usage
```
seqExtractor.py [-h] -i INPUT (-l ID_LIST | -s SUBSTRING) -o OUTPUT [-t THREADS] [-c]

Extract fasta sequence records from multiFASTA file based on a list of record ids or a substring in the sequence header

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename include extension of original FASTA file
  -l ID_LIST, --id_list ID_LIST
                        Filename include extension of the sequence ID list
  -s SUBSTRING, --substring SUBSTRING
                        Substring to search for in the sequence header
  -o OUTPUT, --output OUTPUT
                        Filename include extension of output FASTA file
  -t THREADS, --threads THREADS
                        Number of threads to use (default: 1)
  -c, --case_insensitive
                        Make the substring search case insensitive (default: False)
```
There are two ways to use seqExtractor tool: 
  - Extract sequences based on a list of sequence IDs: 
    ```
    python seqExtractor.py -i input.fasta -l id_list.txt -o output.fasta -t 4
    ```

  - Extract sequences based on a substring in the sequence header: 
    - case sensitive (by default)
      ```
      python seqExtractor.py -i input.fasta -s Belgium -o output.fasta -t 4
      ```
    
    - case insensitive
      ```
      python seqExtractor.py -i input.fasta -s belgium -o output.fasta -t 4 --case-insensitive
      ```

---

## Motivation and goal



## Inspiration 
Inspired by [faSomeRecords from Santiago Sanchez-Ramirez](https://github.com/santiagosnchez/faSomeRecords), which firstly created by kentUtils in C++ version.

---

## Found a bug?
Or would like a feature added? Or maybe drop some feedback? Just open a new issue or send an email to us (lichuinchong@gmail.com).
