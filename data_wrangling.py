import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('RewardsData.csv')
not_available=df.isna()
print(not_available.sum())
percentage=not_available.sum()/len(df)*100
print(percentage)
print(df['Last Seen'].head())
df['Last Seen']=pd.to_datetime(df['Last Seen'])
print(df['Last Seen'].head())
df['Last Seen']=df['Last Seen'].fillna(value=df['Last Seen'].min())
print(df.isna().sum())
df.dropna(inplace=True)
print(df.isna().sum())
print(df.shape)
df.drop(columns='Tags',inplace=True)
print(df.shape)
unique_cities=df['City'].unique()
print(unique_cities)
df['City'].replace(to_replace=['Winston salem ' ,'Winston salem' 'Winston-salem','winston salem ','Winston-Salem, NC'],value='Winston-Salem',inplace=True)
df['City']=df['City'].str.strip()
df['City']=df['City'].str.title()
unique_states=df['State'].unique()
print('Unique States',unique_states)
us_states = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}
for state_name in us_states:
    df['State'].replace(to_replace=state_name,value=us_states[state_name],inplace=True)

unique_states=df['State'].unique()
unique_states.sort()
print(unique_states)
df.loc[df['State']=='District of Columbia']='DOC'
unique_states=df['State'].unique()
unique_states.sort()
print(unique_states)
states_df=pd.DataFrame(list(us_states.items()),columns=[
    'State Name','State'
])
print(states_df.head())
df=pd.merge(df,states_df,on='State',how='left')
print(df.head())
df.rename(columns={'State':'State Abbreviation'},inplace=True)
print(df.head())
state_col=df.pop('State Name')
df.insert(3,'State Name',state_col)
print(df.head())
df['Zip']=df['Zip'].str[:5]
boolean_index=df['Zip'].str.len()==5
df=df[boolean_index]
df=df[df["City"]!='G']
df=df[df['City']!='Lmao']
print(len(df))
duplicates=df.duplicated()
print(duplicates.sum())
clean_duplicates=df.drop_duplicates()
duplicates=clean_duplicates.duplicated()
print(duplicates.sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
print(df.duplicated().sum())
state_points = (
    df.groupby('State Name')['Total Points Earned']
    .sum()
    .sort_values(ascending=True)
)

plt.figure()
plt.bar(state_points.index, state_points.values)
plt.xticks(rotation=45)
plt.xlabel('State')
plt.ylabel('Total Points Earned')
plt.title('Top 10 States by Total Points Earned')
plt.tight_layout()
plt.show()

plt.figure()
plt.hist(df['Available Points'], bins=20)
plt.xlabel('Available Points')
plt.ylabel('Number of Users')
plt.title('Distribution of Available Points')
plt.show()

plt.figure()
plt.scatter(df['Available Points'], df['Total Points Earned'], alpha=0.6)
plt.xlabel('Available Points')
plt.ylabel('Total Points Earned')
plt.title('Available Points vs Total Points Earned')
plt.show()
state_users = df['State Name'].value_counts().head(10)

plt.figure()
plt.bar(state_users.index, state_users.values)
plt.xticks(rotation=45)
plt.xlabel('State')
plt.ylabel('Number of Users')
plt.title('Top 10 States by User Count')
plt.tight_layout()
plt.show()

plt.figure()
plt.boxplot(df['Total Points Earned'])
plt.ylabel('Total Points Earned')
plt.title('Distribution of Total Points Earned')
plt.show()



