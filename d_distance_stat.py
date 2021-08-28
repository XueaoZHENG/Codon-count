from d_list_distance import distance_list
def distance_stat(seq,id):

    # seq = "ATGGAGGATCAAGTTGGGTTTGGGTTCCGTCCGAACGACGAGGAGCTCGTTGGTCACTATCTCCGTAACAAAATCGAAGGAAACACTAGCCGCGACGTTGAAGTAGCCATCAGCGAGGTCAACATCTGTAGCTACGATCCTTGGAACTTGCGCTTCCAGTCAAAGTACAAATCGAGAGATGCTATGTGGTACTTCTTCTCTCGTAGAGAAAACAACAAAGGGAATCGACAGAGCAGGACAACGGTTTCTGGTAAATGGAAGCTTACCGGAGAATCTGTTGAGGTCAAGGACCAGTGGGGATTTTGTAGTGAGGGCTTTCGTGGTAAGATTGGTCATAAAAGGGTTTTGGTGTTCCTCGATGGAAGATACCCTGACAAAACCAAATCTGATTGGGTTATCCACGAGTTCCACTACGACCTCTTACCAGAACATCAGAGGACATATGTCATCTGCAGACTTGAGTACAAGGGTGATGATGCGGACATTCTATCTGCTTATGCAATAGATCCCACTCCCGCTTTTGTCCCCAATATGACTAGTAGTGCAGGTTCTGTGGTCAACCAATCACGTCAACGAAATTCAGGATCTTACAACACTTACTCTGAGTATGATTCAGCAAATCATGGCCAGCAGTTTAATGAAAACTCTAACATTATGCAGCAGCAACCACTTCAAGGATCATTCAACCCTCTCCTTGAGTATGATTTTGCAAATCACGGCGGTCAGTGGCTGAGTGACTATATCGACCTGCAACAGCAAGTTCCTTACTTGGCACCTTATGAAAATGAGTCGGAGATGATTTGGAAGCATGTGATTGAAGAAAATTTTGAGTTTTTGGTAGATGAAAGGACATCTATGCAACAGCATTACAGTGATCACCGGCCCAAAAAACCTGTGTCTGGGGTTTTGCCTGATGATAGCAGTGATACTGAAACTGGATCAATGATTTTCGAAGACACTTCGAGCTCCACTGATAGTGTTGGTAGTTCAGATGAACCGGGCCATACTCGTATAGATGATATTCCATCATTGAACATTATTGAGCCTTTGCACAATTATAAGGCACAAGAGCAACCAAAGCAGCAGAGCAAAGAAAAGGTGATAAGTTCGCAGAAAAGCGAATGCGAGTGGAAAATGGCTGAAGACTCGATCAAGATACCTCCATCCACCAACACGGTGAAGCAGAGCTGGATTGTTTTGGAGAATGCACAGTGGAACTATCTCAAGAACATGATCATTGGTGTCTTGTTGTTCATCTCCGTCATTAGTTGGATCATTCTTGTTGGTTAA"

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []
    list20 = []
    list21 = []
    list22 = []
    list23 = []
    list24 = []
    list25 = []
    list26 = []
    list27 = []
    list28 = []
    list29 = []
    list30 = []
    list31 = []
    list32 = []
    list33 = []
    list34 = []
    list35 = []
    list36 = []
    list37 = []
    list38 = []
    list39 = []
    list40 = []
    list41 = []
    list42 = []
    list43 = []
    list44 = []
    list45 = []
    list46 = []
    list47 = []
    list48 = []
    list49 = []
    list50 = []
    list51 = []
    list52 = []
    list53 = []
    list54 = []
    list55 = []
    list56 = []
    list57 = []
    list58 = []
    list59 = []
    list60 = []
    list61 = []
    list62 = []
    list63 = []
    list64 = []

    table_cal_p = {
        'ATA': list1, 'ATC': list2, 'ATT': list3, 'ATG': list4,
        'ACA': list5, 'ACC': list6, 'ACG': list7, 'ACT': list8,
        'AAC': list9, 'AAT': list10, 'AAA': list11, 'AAG': list12,
        'AGC': list13, 'AGT': list14, 'AGA': list15, 'AGG': list16,
        'CTA': list17, 'CTC': list18, 'CTG': list19, 'CTT': list20,
        'CCA': list21, 'CCC': list22, 'CCG': list23, 'CCT': list24,
        'CAC': list25, 'CAT': list26, 'CAA': list27, 'CAG': list28,
        'CGA': list29, 'CGC': list30, 'CGG': list31, 'CGT': list32,
        'GTA': list33, 'GTC': list34, 'GTG': list35, 'GTT': list36,
        'GCA': list37, 'GCC': list38, 'GCG': list39, 'GCT': list40,
        'GAC': list41, 'GAT': list42, 'GAA': list43, 'GAG': list44,
        'GGA': list45, 'GGC': list46, 'GGG': list47, 'GGT': list48,
        'TCA': list49, 'TCC': list50, 'TCG': list51, 'TCT': list52,
        'TTC': list53, 'TTT': list54, 'TTA': list55, 'TTG': list56,
        'TAC': list57, 'TAT': list58, 'TAA': list59, 'TAG': list60,
        'TGC': list61, 'TGT': list62, 'TGA': list63, 'TGG': list64}
    # seq1 = "ATGGAGGATCAAGTTGGGTTTGGGTTCCGTCCGAACGACGAGGAGCTCGTTGGTCACTATCTCCGTAACAAAATCGAAGGAAACACTAGCCGCGACGTTGAAGTAGCCATCAGCGAGGTCAACATCTGTAGCTACGATCCTTGGAACTTGCGCTTCCAGTCAAAGTACAAATCGAGAGATGCTATGTGGTACTTCTTCTCTCGTAGAGAAAACAACAAAGGGAATCGACAGAGCAGGACAACGGTTTCTGGTAAATGGAAGCTTACCGGAGAATCTGTTGAGGTCAAGGACCAGTGGGGATTTTGTAGTGAGGGCTTTCGTGGTAAGATTGGTCATAAAAGGGTTTTGGTGTTCCTCGATGGAAGATACCCTGACAAAACCAAATCTGATTGGGTTATCCACGAGTTCCACTACGACCTCTTACCAGAACATCAGAGGACATATGTCATCTGCAGACTTGAGTACAAGGGTGATGATGCGGACATTCTATCTGCTTATGCAATAGATCCCACTCCCGCTTTTGTCCCCAATATGACTAGTAGTGCAGGTTCTGTGGTCAACCAATCACGTCAACGAAATTCAGGATCTTACAACACTTACTCTGAGTATGATTCAGCAAATCATGGCCAGCAGTTTAATGAAAACTCTAACATTATGCAGCAGCAACCACTTCAAGGATCATTCAACCCTCTCCTTGAGTATGATTTTGCAAATCACGGCGGTCAGTGGCTGAGTGACTATATCGACCTGCAACAGCAAGTTCCTTACTTGGCACCTTATGAAAATGAGTCGGAGATGATTTGGAAGCATGTGATTGAAGAAAATTTTGAGTTTTTGGTAGATGAAAGGACATCTATGCAACAGCATTACAGTGATCACCGGCCCAAAAAACCTGTGTCTGGGGTTTTGCCTGATGATAGCAGTGATACTGAAACTGGATCAATGATTTTCGAAGACACTTCGAGCTCCACTGATAGTGTTGGTAGTTCAGATGAACCGGGCCATACTCGTATAGATGATATTCCATCATTGAACATTATTGAGCCTTTGCACAATTATAAGGCACAAGAGCAACCAAAGCAGCAGAGCAAAGAAAAGGTGATAAGTTCGCAGAAAAGCGAATGCGAGTGGAAAATGGCTGAAGACTCGATCAAGATACCTCCATCCACCAACACGGTGAAGCAGAGCTGGATTGTTTTGGAGAATGCACAGTGGAACTATCTCAAGAACATGATCATTGGTGTCTTGTTGTTCATCTCCGTCATTAGTTGGATCATTCTTGTTGGTTAA"

    c = int(len(seq) / 3)
    for i in range(c):
        codon = seq[3 * i: 3 * i + 3]
        table_cal_p[codon].append(i + 1)
    f = len(table_cal_p["TAA"]) + len(table_cal_p["TAG"]) + len(table_cal_p["TGA"])
    if f <= 1:
        list001=[distance_list(table_cal_p[key]) for key in table_cal_p.keys()]

        # list002 = list001 + [distance_list(table_cal_p["GAA"] + table_cal_p["CAA"] + table_cal_p["AAA"])]+[distance_list(table_cal_p["GAA"] + table_cal_p["CAA"])]+[distance_list(table_cal_p["CAA"] + table_cal_p["AAA"])]+[distance_list(table_cal_p["GAA"] + table_cal_p["AAA"])]+[[c] * 4]+[[id] * 4]
        list001.append(distance_list(table_cal_p["GAA"] + table_cal_p["CAA"] + table_cal_p["AAA"]))
        list001.append(distance_list(table_cal_p["GAA"] + table_cal_p["CAA"]))
        list001.append(distance_list(table_cal_p["CAA"] + table_cal_p["AAA"]))
        list001.append(distance_list(table_cal_p["GAA"] + table_cal_p["AAA"]))
        list001.append([c] * 4)
        list001.append([id] * 4)
        # list002.extend(list003)
        # list003 = [list001] + [list002]
    else:
        list001 = [[0, 0, 0, 0]] * 70
        print(id , "'s stop codon is over 1  !!!")
    return list001


    ### df0 = pd.DataFrame()
    # if f <= 1:
    #     for key in table_cal_p.keys():
    #         df0[key] = distance_list(table_cal_p[key])

    ###计算s2距离list
    # df0["s2_Count"] = distance_list(table_cal_p["GAA"] + table_cal_p["CAA"] + table_cal_p["AAA"])
    # df0["G_C_Count"] = distance_list(table_cal_p["GAA"] + table_cal_p["CAA"])
    # df0["A_C_Count"] = distance_list(table_cal_p["AAA"] + table_cal_p["CAA"])
    # df0["G_A_Count"] = distance_list(table_cal_p["GAA"] + table_cal_p["AAA"])
    # df0["Total_aa"] = c
    # df0["ID"] = id
    # print(df0)
    # dict01 = df0.to_dict("split")
    # return dict01

    ### 第二种
    # list002 = []
    # list003 = ["s2codon", "GAA_CAA", "CAA_AAA", "GAA_AAA", "Total_aa", "ID"]