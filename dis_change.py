import pandas as pd
import os
import numpy as np

dir = r"D:\codon_distance\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
file1 = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.csv"
file2 = "count_discribe.csv"
file3 = "Sc_fre_descri.csv"
os.chdir(dir)

df_med = pd.read_csv(file1,index_col=0) # 这里要小心表格类型的问题
df_med =df_med.loc[df_med["stat"]=="count",:]
df_med =df_med.loc[df_med["Total_aa"]!=0,:]
df_med =df_med.iloc[:,0:69]

df_med.replace(0,np.nan,inplace = True)
print(df_med)
df_med.describe().to_csv(file2)
# print("Mission completed!!!")
# df01 = df_med.iloc[:,0:69]/df_med["Total_aa"]

# df01 = pd.DataFrame()
# for column in df_med.columns.values:
#     df01[column] = df_med.apply(lambda x:x[column]/x["Total_aa"], axis = 1)
# print(df01)
# df01.to_csv(file2)
# df01.describe().to_csv(file3)


