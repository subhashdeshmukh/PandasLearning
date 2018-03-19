#contacting two csv files using pandas

import pandas as pd

csv_files = ['first.csv','second.csv']

final_df = pd.DataFrame()

for file in csv_files:
    df = pd.read_csv(file,sep='\t')
    final_df = pd.concat([final_df,df])

#print final_df.head(10)
final_df['source'] = 'first.csv'

print(final_df.head())



