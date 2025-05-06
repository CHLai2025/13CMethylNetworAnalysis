import os
import pandas as pd

current_directory = os.path.dirname(__file__)

# Define the list of strings to be removed
remove_strings = ["CD1-HD1", "CD2-HD2", "CE-HE", "CG1-HG1", "CG2-HG2", "CB-HB"]

# Save all processed data
all_data = []

# Read and process each file
for filename in os.listdir(current_directory):
    if filename.endswith(".txt"):
        with open(os.path.join(current_directory, filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split("\t")
                if len(parts) == 3:
                    # Remove strings
                    for remove_string in remove_strings:
                        parts[0] = parts[0].replace(remove_string, "")
                    # Extract the required information and perform the conversion
                    new_line = [parts[0], parts[1], parts[2].split('_')[0]]
                    all_data.append(new_line)

# Convert the data into a DataFrame
df = pd.DataFrame(all_data)

# Write the DataFrame to an Excel file.
output_filename = "connection.xlsx"
output_filepath = os.path.join(current_directory, output_filename)
df.to_excel(output_filepath, index=False, header=False)
