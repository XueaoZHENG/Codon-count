from Bio import SeqIO
import pandas as pd
from find_stopcodon_targetcodon import count_s2_codon

b = 0
c = 0
d = 0
g = 0
list_GAA_CAA_AAA_T = []
dict_GAA_CAA_AAA_T = {}
str1 = ""

for seq_record in SeqIO.parse(r"C:\Users\31781\Desktop\cal_codon\Araport11_genes.201606.cds.fasta", "fasta"):
    b = b + 1
    seq1 = "" + seq_record.seq
    ff = seq1.find("TAA") + seq1.count("TAG") + seq1.count("TGA")

    if len(seq_record) % 3 == 0:  # find the non-orf seq and add to list
        c = c + 1
        list_GAA_CAA_AAA_T = count_s2_codon(seq_record)
        dict_GAA_CAA_AAA_T[seq_record.id] = list_GAA_CAA_AAA_T
    else:
        d = d + 1

# print("There are ",len(b),"non-orf seqs")
dict1 = dict_GAA_CAA_AAA_T
print("Number of total seqs:", b)
print("Number of non-orf seqs:", d)
print("Number of multiple stopcodon seqs:", g)

#  SeqIO.write(a, r"C:\Users\31781\Desktop\cal_codon\Araport11_genes.201606.cds_flt.fasta", "fasta")

data1 = pd.DataFrame(dict1)
print(data1)
data1.to_csv(r"C:\Users\31781\Desktop\cal_codon\GAA_CAA_AAA.csv", header=True,index=True)