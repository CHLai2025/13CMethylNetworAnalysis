import os
import pandas as pd


merged_df = pd.DataFrame()

data_folder = "pkm2std_output"

# Use the os module to list all text files in the folder
for file_name in os.listdir(data_folder):
    if file_name.endswith(".txt"):
        file_path = os.path.join(data_folder, file_name)
        df = pd.read_csv(file_path, sep="\t")
        
        # Add the file name to the DataFrame to differentiate the data
        df["file_name"] = file_name
        
        # Merge the data into the main DataFrame
        merged_df = pd.concat([merged_df, df], ignore_index=True)

# Write the merged data into a new text file
merged_df.to_csv("merged_data.txt", sep="\t", index=False)
