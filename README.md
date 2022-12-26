# seqExtractor
A python tool to extract multiple fasta sequence records from multiFASTA file based on a list of record ids. <br>
Written by: [Li Chuin Chong](https://github.com/ChongLC) and [Yeo Keat Ee](https://github.com/ee2110)

---

## Usage
```
seqExtractor.py [-h] -i INPUT -l ID_LIST -o OUTPUT [-t THREADS]

Extract fasta sequence records from multiFASTA file based on a list of record ids

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename include extension of original FASTA file
  -l ID_LIST, --id_list ID_LIST
                        Filename include extension of the sequence ID list
  -o OUTPUT, --output OUTPUT
                        Filename include extension of output FASTA file
  -t THREADS, --threads THREADS
                        Number of threads to use (default: 1)

```
In the usage case below, the seqExtractor tool is applied to extract fasta sequences based on the id list (`id_list.txt`) from the input multiFASTA file (`exampleinput.fasta`), resulting an output file (`exampleoutput.fasta`).  
```
python seqExtractor.py -i exampleinput.fasta -l id_list.txt -o exampleoutput.fasta -t 2
```

---

## Installation
1. Download only the python code <br>
    ```
    wget https://raw.githubusercontent.com/ChongLC/seqExtractor/master/seqExtractor.py
    ```

2. Download the entire repo

---

## Motivation and goal



## Inspiration 
Inspired by [faSomeRecords from Santiago Sanchez-Ramirez](https://github.com/santiagosnchez/faSomeRecords), which firstly created by kentUtils in C++ version.

---

## Found a bug?
Or would like a feature added? Or maybe drop some feedback? Just open a new issue or send an email to us (lichuinchong@gmail.com).
