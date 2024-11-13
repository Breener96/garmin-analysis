import pandas as pd

df = pd.read_csv('/Users/gracebreen/GitHub_Projects/garmin-analysis/data/Activities.csv')



# Exclude any activity that isn't a run
df_filtered = df[df['Activity Type'] != 'Running']

#Removing redundant fields
df = df.drop(['Activity Type','Decompression', 'Favorite'], axis=1)


print(df.head())
