def count_s2_codon(seq_record):
    seq1 = seq_record.seq
    c = 0
    d = 0
    f = 0
    g = 0
    codon_GAA = 0
    codon_CAA = 0
    codon_AAA = 0
    Total = 0
    codon = ""
    seql_split = []
    seql_sub = []
    list_GAA_CAA_AAA_T = []
    dict_ref ={"AAA":"AAG","GAA":"GAG","CAA":"CAG"}
    dict_GAA_CAA_AAA_T = {}

    seq_lens = 0

    #  seq1 = "ATGGAGGATCAAGTTGGGTTTGGGTTCCGTCCGAACGACGAGGAGCTCGTTGGTCACTATCTCCGTAACAAAATCGAAGGAAACACTAGCCGCGACGTTGAAGTAGCCATCAGCGAGGTCAACATCTGTAGCTACGATCCTTGGAACTTGCGCTTCCAGTCAAAGTACAAATCGAGAGATGCTATGTGGTACTTCTTCTCTCGTAGAGAAAACAACAAAGGGAATCGACAGAGCAGGACAACGGTTTCTGGTAAATGGAAGCTTACCGGAGAATCTGTTGAGGTCAAGGACCAGTGGGGATTTTGTAGTGAGGGCTTTCGTGGTAAGATTGGTCATAAAAGGGTTTTGGTGTTCCTCGATGGAAGATACCCTGACAAAACCAAATCTGATTGGGTTATCCACGAGTTCCACTACGACCTCTTACCAGAACATCAGAGGACATATGTCATCTGCAGACTTGAGTACAAGGGTGATGATGCGGACATTCTATCTGCTTATGCAATAGATCCCACTCCCGCTTTTGTCCCCAATATGACTAGTAGTGCAGGTTCTGTGGTCAACCAATCACGTCAACGAAATTCAGGATCTTACAACACTTACTCTGAGTATGATTCAGCAAATCATGGCCAGCAGTTTAATGAAAACTCTAACATTATGCAGCAGCAACCACTTCAAGGATCATTCAACCCTCTCCTTGAGTATGATTTTGCAAATCACGGCGGTCAGTGGCTGAGTGACTATATCGACCTGCAACAGCAAGTTCCTTACTTGGCACCTTATGAAAATGAGTCGGAGATGATTTGGAAGCATGTGATTGAAGAAAATTTTGAGTTTTTGGTAGATGAAAGGACATCTATGCAACAGCATTACAGTGATCACCGGCCCAAAAAACCTGTGTCTGGGGTTTTGCCTGATGATAGCAGTGATACTGAAACTGGATCAATGATTTTCGAAGACACTTCGAGCTCCACTGATAGTGTTGGTAGTTCAGATGAACCGGGCCATACTCGTATAGATGATATTCCATCATTGAACATTATTGAGCCTTTGCACAATTATAAGGCACAAGAGCAACCAAAGCAGCAGAGCAAAGAAAAGGTGATAAGTTCGCAGAAAAGCGAATGCGAGTGGAAAATGGCTGAAGACTCGATCAAGATACCTCCATCCACCAACACGGTGAAGCAGAGCTGGATTGTTTTGGAGAATGCACAGTGGAACTATCTCAAGAACATGATCATTGGTGTCTTGTTGTTCATCTCCGTCATTAGTTGGATCATTCTTGTTGGTTAA"


    c = int(len(seq1) / 3)

    for i in range(c):
        codon = seq1[3 * i: 3 * i + 3]

        seql_split.append(codon)
        i = i + 1



    f = seql_split.count("TAA") + seql_split.count("TAG") + seql_split.count("TGA")

    if f <= 1:
        codon_GAA = seql_split.count("GAA")
        codon_CAA = seql_split.count("CAA")
        codon_AAA = seql_split.count("AAA")
        Total = codon_GAA + codon_CAA + codon_AAA
        seq_lens = c
    else:
        g = g + 1
        print(seq_record.id, "contains more than one stop codons！")


    list_GAA_CAA_AAA_T.append(codon_GAA)
    list_GAA_CAA_AAA_T.append(codon_CAA)
    list_GAA_CAA_AAA_T.append(codon_AAA)
    list_GAA_CAA_AAA_T.append(Total)
    list_GAA_CAA_AAA_T.append(seq_lens)
    dict_GAA_CAA_AAA_T[seq_record.id] = list_GAA_CAA_AAA_T
    #  print(seq_record.id, dict_GAA_CAA_AAA_T[seq_record.id])
    return list_GAA_CAA_AAA_T











