from Bio import SeqIO
import numpy as np
from d_distance_stat import distance_stat

def flow(file):
    # start = datetime.now()
    b = 0
    c = 0
    d = 0
    np0 = np.empty([0, 70])
    # file1 = r"test.txt"
    ## 第二种写法 0.1秒
    for seq_record in SeqIO.parse(file, "fasta"):
        if len(seq_record.seq) % 3 == 0:  # find the non-orf seq and add to list
            np1 = np.asarray(distance_stat(seq_record.seq, seq_record.id)).T
            np0 = np.append(np1, np0, axis=0)
            c = c + 1
            # list2.append(distance_stat(seq1,seq_record.id))
        else:
            d = d + 1
    return np0

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




    # list3 = ['ATA', 'ATC', 'ATT', 'ATG', 'ACA', 'ACC', 'ACG', 'ACT', 'AAC', 'AAT', 'AAA', 'AAG', 'AGC', 'AGT', 'AGA', 'AGG', 'CTA', 'CTC', 'CTG', 'CTT', 'CCA', 'CCC', 'CCG', 'CCT', 'CAC', 'CAT', 'CAA', 'CAG', 'CGA', 'CGC', 'CGG', 'CGT', 'GTA', 'GTC', 'GTG', 'GTT', 'GCA', 'GCC', 'GCG', 'GCT', 'GAC', 'GAT', 'GAA', 'GAG', 'GGA', 'GGC', 'GGG', 'GGT', 'TCA', 'TCC', 'TCG', 'TCT', 'TTC', 'TTT', 'TTA', 'TTG', 'TAC', 'TAT', 'TAA', 'TAG', 'TGC', 'TGT', 'TGA', 'TGG', 's2codon', 'GAA_CAA', 'CAA_AAA', 'GAA_AAA', 'Total_aa', 'ID']
    # df0001 = pd.DataFrame(np0,columns=list3)
    # df0001["stat"] = ["count", "mean", "med", "std"]*c
    # print(df0001.head(20))
    # # print(list00)
    # print("Number of non-orf seqs:", d)
    #
    # # print("Time:", (datetime.now() - start))
    #
    #
    # # df0001.to_csv(r"GCF_000002985.6_WBcel235_rna.fna_Ce\GCF_000002985.6_WBcel235_rna.fna.csv")
    # # df_med = pd.DataFrame()
    # # df_med =df0001.loc[df0001["stat"]=="med",:]
    # # df_med.describe().to_csv(r"test_des.csv")