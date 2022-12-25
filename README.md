# seqExtractor
A python tool to extract multiple fasta sequence records from multiFASTA file based on a list of record ids. <br>
Written by: [Li Chuin Chong](https://github.com/ChongLC) and [Yeo Keat Ee](https://github.com/ee2110)

---

## Usage
```
python seqExtractor.py [-h] [-i INPUT] [-o OUTPUT] [-l ID_LIST]
```
In the usage case below, the seqExtractor tool is applied to extract fasta sequences based on the id list (`id_list.txt`) from the input multiFASTA file (`exampleinput.fasta`), resulting an output file (`exampleoutput.fasta`).  
```
python seqExtractor.py -i exampleinput.fasta -l id_list.txt -o exampleoutput.fasta
```
---

## Motivation and goal



## Inspiration 
Inspired by [faSomeRecords from Santiago Sanchez-Ramirez](https://github.com/santiagosnchez/faSomeRecords), which firstly created by kentUtils in C++ version.

---

## Found a bug?
Or would like a feature added? Or maybe drop some feedback? Just open a new issue or send an email to us (lichuinchong@gmail.com).
