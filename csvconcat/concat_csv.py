#concat two csv files provided they have similar data
#add another column with name of first file
#write this data to the third file

import pandas as pd

csv_files = ['first.csv','second.csv']

final_df = pd.DataFrame()

for file in csv_files:
    df = pd.read_csv(file,sep='\t')
    final_df = pd.concat([final_df,df])

final_df['source'] = 'first.csv'

print(final_df.head())
final_df.to_csv('third.csv',sep='\t')




