# Codon-count
The is a python script to calculate the codon count of a fasta file.
The auther use it to obtain the 64 codon count at the whole genome scale.

If the gene number is over 2000, please use the script "dis_preprocess". Then ,proceed with the "dis_stat" script.

You could provide three input values:

dir = r"D:\codon_distance\mouse\split" ### the fasta file dir
file1 = "Mouse1.csv"  ### the result file name 
file2 = "Mouse1_des.csv" ### the description of result file name 

The calculation results would be save in the fasta file dir.

