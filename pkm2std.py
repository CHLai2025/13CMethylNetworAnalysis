import pandas as pd
import os

# Set the input and output folder paths
input_folder_path = "CSP_output"
output_folder_path = "pkm2std_output"

# Create the output folder (if it does not exist)
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Iterate through all Excel files in the folder.
for filename in os.listdir(input_folder_path):
    if filename.endswith(".xlsx"):
        input_file_path = os.path.join(input_folder_path, filename)
        
        # Read the excel documents
        xl = pd.read_excel(input_file_path, sheet_name=None)
        
        # Iterate through all worksheets
        for sheet_name, df in xl.items():
            # Calculate the mean and standard deviation of the CSPs
            csp_mean = df["Δδ"].mean()
            csp_std = df["Δδ"].std()
            # Calculate the value of AVG+2STD
            avg_2std = csp_mean + 2 * csp_std
            # Filter rows that satisfy both conditions
            filtered_df = df.loc[(df['Δδ'] >= 0.01) & (df['Δδ'] > avg_2std)]
            
            # If there are rows that meet the conditions, write them to the corresponding output file
            if not filtered_df.empty:
                output_file_path = os.path.join(output_folder_path, f"{filename}.txt")
                filtered_df.to_csv(output_file_path, sep='\t', index=False)