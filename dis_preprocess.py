
from Bio import SeqIO
import os
import re

os.chdir(r"D:\codon_distance\mouse\split")
i = 0
n1 = 0
d = 0
log = "log.txt"
file1 = r"D:\codon_distance\mouse\Mus_musculus.GRCm39.cds.all.fa"

for seq_record in SeqIO.parse(file1, "fasta"):
    if i*2000 <= n1 <= 2000 + i*2000:
        n1 = n1 + 1
        file = "Hs" + str(i) + ".txt"
        if seq_record.seq.find("N") == -1 :
            with open(file, 'a+') as f:
                f.write(">"+str(seq_record.name)+"\n"+str(seq_record.seq)+"\n")
        else:
            with open(log, "a+") as f:
                f.write(seq_record.name + "contain NNN !!!" + "\n")
            d = d + 1
    else:
        i = i+1
        print("Processing: file",i)

print("Find", d," NNN seqs")
print("Mission complete!")

