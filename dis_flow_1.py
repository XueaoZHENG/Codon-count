from Bio import SeqIO
import numpy as np
from d_distance_stat import distance_stat

def flow_0(file):
    # start = datetime.now()
    b = 0
    c = 0
    d = 0
    np0 = np.empty([0, 70])
    # file1 = r"test.txt"
    ## 第二种写法 0.1秒
    for seq_record in SeqIO.parse(file, "fasta"):
        np1 = np.asarray(distance_stat(seq_record.seq, seq_record.id)).T
        np0 = np.append(np1, np0, axis=0)
    return np0