from Bio import SeqIO
from d_distance_stat import distance_stat
import numpy as np

def grownp(file1):

    b = 0
    c = 0
    d = 0
    np0 = np.empty([0,70])

    ### 第一种写法 时间：1秒多接近两秒
    # for seq_record in SeqIO.parse(r"C:\Users\31781\Desktop\cal_codon\Araport11_genes.201606.cds_flt_test.fasta", "fasta"):
    #     b = b + 1
    #     seq1 = "" + seq_record.seq
    #     list_index= distance_stat(seq1, seq_record.id)["index"]
    #     list_columns = distance_stat(seq1,seq_record.id)["columns"]
    #     if len(seq_record) % 3 == 0:  # find the non-orf seq and add to list
    #         c = c + 1
    #         np1 = np.asarray(distance_stat(seq1,seq_record.id)["data"])
    #         np0 = np.concatenate((np1,np0),axis=0)
    #     else:
    #         d = d + 1
    # list_index1 = list_index*c
    # df0001 = pd.DataFrame(np0,columns=list_columns)
    # df0001["stat"] = list_index1

    # file1 = open("matrixfile.npy")

    ### 第二种写法 0.1秒
    for seq_record in SeqIO.parse(file1, "fasta"):
        if len(seq_record.seq) % 3 == 0:  # find the non-orf seq and add to list
            np1 = np.asarray(distance_stat(seq_record.seq,seq_record.id)).T
            np0 = np.append(np1,np0,axis=0)
            # np.concatenate((np1,np0),axis=0)
            # list00.append(np1)
            c = c + 1
            # list2.append(distance_stat(seq1,seq_record.id))
        else:
            d = d + 1

    return (np0)