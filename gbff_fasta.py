import pandas as pd
import os
from Bio import SeqIO
from Bio import Seq


os.chdir("D:\codon_distance\GCF_000005845.2_ASM584v2_genomic.gbff_Ec")
record_fa = SeqIO.read("GCF_000005845.2_ASM584v2_genomic.fna", "fasta")
df01 = pd.read_csv("proteins_167_161521.csv", index_col="Protein product")


# print(record_fa.seq)
# print(record_gb)
# print(df01)


s0 =str(record_fa.seq)
df02 = df01.loc[df01["Strand"] == "+",:]
file = "Ecoli_fasta_trans.fa"
with open(file, 'a+') as f:
    for i in df02.index:
        ss1 = s0[df02.loc[i, "Start"] - 1:df02.loc[i, "Stop"]]
        f.write(">" + i + "\n" +ss1 + "\n")


s1 =str(record_fa.seq)
df02 = df01.loc[df01["Strand"] == "-",:]
file1 = "Ecoli_fasta_cis.fa"
with open(file1, 'a+') as f:
    for i in df02.index:
        ss2 = s1[df02.loc[i, "Start"] - 1:df02.loc[i, "Stop"]]
        f.write(">" + i + "\n" +ss2 + "\n")

file2 = "Ecoli_fasta_trans2.fa"


with open(file2, 'a+') as f:
    for seq_record in SeqIO.parse(file1, "fasta"):
        rever = seq_record.reverse_complement()
        f.write(">"+str(seq_record.id)+ "\n" + str(rever.seq) + "\n")


print("Completed！")