import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
 
# Directory containing CSV files
directory = 'temp'
 
# List to store dataframes
dataframes = []
 
# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        print('filename:', filename)
 
        filepath = os.path.join(directory, filename)
        print('filepath:', filepath)
        try:
            # Read CSV file into DataFrame
            df = pd.read_csv(filepath, header=None, names=['server', 'kasa'])
            # Add 'store' column with filename minus '.csv'
 
            tanggal = filename[:8]
            # print('tanggal:', tanggal)
            store = filename[8:].replace('.csv', '')
            # print('store:', store)
 
            df['store'] = store
            df['tanggal'] = pd.to_datetime(tanggal)
            dataframes.append(df)
            print(f"Successfully read {filename}")
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
 
# for d in dataframes:
#     print(d)
 
# Optionally, concatenate all DataFrames into one
if len(dataframes) > 0:
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df = combined_df.sort_values(by=['tanggal'], ascending=True)
    print(combined_df)
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='tanggal', y='server', hue='store', data=combined_df, marker='o', markersize=10)
    sns.lineplot(x='tanggal', y='kasa', hue='store', data=combined_df, marker='s', markersize=10, palette='viridis')
#     # sns.barplot(x='tanggal', y='sales', hue='store', data=combined_df, dodge=False)
 
#     # Set plot labels and title
#     plt.xlabel('Tanggal')
#     plt.ylabel('Sales')
#     plt.title('Sales for All Stores (Grouped by Date)')
#     plt.xticks(rotation=0, ha='right')  # Rotate x-axis labels
#     plt.legend(title='Store')  # Add a legend with a title
    plt.tight_layout()
    # plt.savefig('./result.png')
    plt.show()
    
# else:
#     print('tidak ada csv yang bisa dijadikan dataframe')