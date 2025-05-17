import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import os

directory = './data'

dataframes =[]

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        print('filename:',filename)

        filepath = os.path.join(directory, filename)
        print('filepath:', filepath)
        try:
            df = pd.read_csv(filepath)
            print('before:\n', df)
            df['store'] = filename.replace('.csv', '')
            print('after:\n', df)
            dataframes.append(df)
            print(f"Successfully read {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")    

for d in dataframes:
    print(d)

if len(dataframes) > 0:
#   combined_df = pd.concat(dataframes, ignore_index=True)
   combined_df = combined_df.sort_values(by=['tanggal'], ascending=True)
   for store, store_data in combined_df.groupby('store'):
        store_data = store_data.sort_values(by=['tanggal'], ascending=True)
        print(store_data)
#    print(combined_df)  
#    combined_df = combined_df.sort_values(by='tanggal',ascending=False)  
#    print(combined_df)
#
#    print ("All files combined into a single DataFrame.")
    plt.figure(figsize=(12,6))
    plt.title('BORMA SALES')
    plt.xlabel('Tanggal')
    plt.ylabel('Sales')
    plt.bar(store_data['tanggal'], store_data['sales'], color='violet')
#    sns.barplot(x='tanggal', y='sales', hue='store', data=combined_df)

    plt.savefig(store + '.png')
#    plt.savefig('./result1.png')