import pandas as pd

codon_file =r"C:\Users\31781\Desktop\dis_stat.csv"
df =pd.read_csv(codon_file)
df.fillna(0)
df.to_csv(r"C:\Users\31781\Desktop\dis_stat01.csv")