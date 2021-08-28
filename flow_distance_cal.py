from Bio import SeqIO
import pandas as pd
import numpy as np
from _datetime import datetime
from d_distance_stat import distance_stat
import os
from Bio import GenBank


os.chdir("D:\codon_distance\GCF_000005845.2_ASM584v2_genomic.gbff_Ec")
file1 = r"Ecoli_fasta_trans.fa"
start = datetime.now()
b = 0
c = 0
d = 0
np0 = np.empty([0, 70])
# file1 = r"test.txt"
start = datetime.now()


## 第二种写法 0.1秒parse
for seq_record in SeqIO.parse(file1, "fasta"):
    if len(seq_record.seq) % 3 == 0:  # find the non-orf seq and add to list
        np1 = np.asarray(distance_stat(seq_record.seq, seq_record.id)).T
        np0 = np.append(np1, np0, axis=0)
        # np.concatenate((np1,np0),axis=0)
        # list00.append(np1)
        c = c + 1
        # list2.append(distance_stat(seq1,seq_record.id))
    else:
        d = d + 1


list3 = ['ATA', 'ATC', 'ATT', 'ATG', 'ACA', 'ACC', 'ACG', 'ACT', 'AAC', 'AAT', 'AAA', 'AAG', 'AGC', 'AGT', 'AGA', 'AGG', 'CTA', 'CTC', 'CTG', 'CTT', 'CCA', 'CCC', 'CCG', 'CCT', 'CAC', 'CAT', 'CAA', 'CAG', 'CGA', 'CGC', 'CGG', 'CGT', 'GTA', 'GTC', 'GTG', 'GTT', 'GCA', 'GCC', 'GCG', 'GCT', 'GAC', 'GAT', 'GAA', 'GAG', 'GGA', 'GGC', 'GGG', 'GGT', 'TCA', 'TCC', 'TCG', 'TCT', 'TTC', 'TTT', 'TTA', 'TTG', 'TAC', 'TAT', 'TAA', 'TAG', 'TGC', 'TGT', 'TGA', 'TGG', 's2codon', 'GAA_CAA', 'CAA_AAA', 'GAA_AAA', 'Total_aa', 'ID']
df0001 = pd.DataFrame(np0,columns=list3)
df0001["stat"] = ["count", "mean", "med", "std"]*c
print(df0001.head(20))
# print(list00)
print("Number of non-orf seqs:", d)
print("Time:", (datetime.now() - start))

df0001.to_csv(r"GCF_000005845.2_ASM584v2_genomic.gbff_Ec.csv")
df0001.index=[i for i in df0001["ID"]]

df_med = pd.DataFrame()
df_med = df0001.loc[df0001["stat"] == "med", :]
df_med.describe().to_csv(r"test_des.csv")
print(df_med)


