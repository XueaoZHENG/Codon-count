import numpy as np
from dis_flow_1 import flow_0
import pandas as pd
import os


dir = r"D:\codon_distance\mouse\split"
file1 = "Mouse1.csv"
file2 = "Mouse1_des.csv"

os.chdir(dir) ### 这个部分要完全一致
np0 = np.empty([0, 70])


for root,dirs,files in os.walk(dir):
    for file in files:#获取目录的名称
        print("Processing",str(file), "file")
        np1 = flow_0(file)
        np0 = np.append(np1, np0, axis=0)

list3 = ['ATA', 'ATC', 'ATT', 'ATG', 'ACA', 'ACC', 'ACG', 'ACT', 'AAC', 'AAT', 'AAA', 'AAG', 'AGC', 'AGT', 'AGA',
         'AGG', 'CTA', 'CTC', 'CTG', 'CTT', 'CCA', 'CCC', 'CCG', 'CCT', 'CAC', 'CAT', 'CAA', 'CAG', 'CGA', 'CGC',
         'CGG', 'CGT', 'GTA', 'GTC', 'GTG', 'GTT', 'GCA', 'GCC', 'GCG', 'GCT', 'GAC', 'GAT', 'GAA', 'GAG', 'GGA',
         'GGC', 'GGG', 'GGT', 'TCA', 'TCC', 'TCG', 'TCT', 'TTC', 'TTT', 'TTA', 'TTG', 'TAC', 'TAT', 'TAA', 'TAG',
         'TGC', 'TGT', 'TGA', 'TGG', 's2codon', 'GAA_CAA', 'CAA_AAA', 'GAA_AAA', 'Total_aa', 'ID']

df0001 = pd.DataFrame(np0, columns=list3)
print(df0001.shape[0])
df0001["stat"] = ["count", "mean", "med", "std"] * (int(df0001.shape[0]/4))

df0001.index = [i for i in df0001["ID"]]
df0001.to_csv(file1)  ### 修改
print(df0001)

df_med = pd.read_csv(file1,index_col = "ID") # 这里要小心表格类型的问题
df_med =df_med.loc[df_med["stat"] == "med",:]
df_med.describe().to_csv(file2)
print("Mission completed!!!")




# df_med.loc[df_med["Total_aa"]>0,:].describe().to_csv(r"ce_des.csv")
# if __name__ == '__main__':
#     p = Pool(6)  # 创建含有十个10个进程的进程池
#     np0 = np.empty([0, 70])  # 存放每一个进程返回的结果
#     # Dm = r'D:\codon_distance\GCF_000001405.39_GRCh38.p13_rna.fna_Hs'
#     # for files in os.walk(Dm):
#     for i in list1:  # 启动10个进程
#         np1 = p.apply(flow,(i,))  # 产生一个非同步进程，函数newsin的参数用args传递
#         np0 = np.append(np1, np0, axis=0)
#
#         # results.append(r)  # 将返回结果放入results
#     p.close()  # 关闭进程池
#     p.join()  # 结束