import pandas as pd
import matplotlib as plt
df=pd.read_csv('pokemon.csv')
print(df.shape)
print(df.head(3))
print(df.duplicated().sum())
print(df.isna().sum())
percentage=df.isna().sum()/len(df)*100