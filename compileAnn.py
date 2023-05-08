import os
import csv
import pandas as pd

# Specify the directory where the ANN files are located
folder_path = 'AnnFiles'
file_list = os.listdir(folder_path)
# Create a list to hold the extracted data from each file
dfs = []

# Iterate over all the ANN files in the directory
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_csv(file_path, sep='^([^\s]*)\s', engine='python',encoding='utf-8', header=None).drop(0, axis=1)
    #add this new (temp during the looping) frame to the end of the list
    dfs.append(df)

#handle a list that is empty
if len(dfs) == 0:
    print('No files found.')
    #create a dummy frame
    df = pd.DataFrame()
#or have only one item/frame and get it out
elif len(dfs) == 1:
    df = dfs[0]
#or concatenate more than one frame together
else: #modify this join as required.
    df = pd.concat(dfs, ignore_index=True)
    df = df.reset_index(drop=True)

new_cols = df[2].str.split(' ', n=3, expand=True)
df[['Label', 'Start', 'End', 'Text']] = new_cols

# Drop the original second column
df.drop(columns=[2], inplace=True)
df = df.rename(columns={1: 'ann_id'})

df['FileNo'] = None
fileno = 0
for i in range(len(df)):
    if df['ann_id'][i] == 'T1':
        fileno += 1
        df['FileNo'][i] = fileno
    else:
        df['FileNo'][i] = fileno

#check what you've got
print(df.head())
df.to_csv('combined_data.csv', index=False)
