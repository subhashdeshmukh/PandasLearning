
#this is the case
#concat two csv files provided they have similar data
#add another column with name of first file
#write this data to the third file

import pandas as pd
import math


# the list of csv sample files
csv_files = ['first.csv','second.csv']

# create an empty dataframe
final_df = pd.DataFrame()

# read the file in the pandas dataframe
for file in csv_files:
    df = pd.read_csv(file,sep='\t')
    final_df = pd.concat([final_df,df])


final_df['source'] = 'first.csv'

# printing the top rows of the dataframe
print(final_df.head())
final_df.to_csv('third.csv',sep='\t')





