import pandas as pd
df=pd.read_csv('RewardsData.csv')
print(df.loc[df['State'].str.strip()=='Mississippi'].head())
print(list(df.columns))
print(df.dtypes)
df['Available Points']=df['Available Points'].astype(float)
print(df.dtypes)
locations=df[['City','State','Zip']]
print(locations.shape)
print(df.iloc[1:4])
df.set_index('State',inplace=True)
print(df.head(2))
georgia_df=df.loc['Georgia']
print(georgia_df.shape)
print(georgia_df.describe())
top_df=df.loc[df['Total Points Earned']>25000]
print(top_df.shape)
print(top_df.sort_values(by=['Total Points Earned'] ,ascending=False))