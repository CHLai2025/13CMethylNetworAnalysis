import pandas as pd
import os

def calculate_delta(input_folder, output_folder):
    # Ensure the output folder exists; create it if it does not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read all Excel files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):
            excel_file = os.path.join(input_folder, filename)
            excel_data = pd.read_excel(excel_file, sheet_name=None)

            # Create an empty list to store the calculation results
            output_dfs = {}

            # Iterate through all sheets
            for sheet_name, sheet_data in excel_data.items():
                if sheet_name == "WT":
                    continue

                # Define the 'WT' sheet
                wt_sheet = excel_data.get("WT", None)
                if wt_sheet is None:
                    print(f"Error: No 'WT' sheet")
                    continue

                # Extract the values from the WT sheet
                wt_values = wt_sheet.iloc[:, 1:].values.astype(float)

                # Calculate δ¹³C and δ¹H
                sheet_values = sheet_data.iloc[:, 1:].values.astype(float)
                delta_values = ((sheet_values - wt_values) / [18, 2.6]) ** 2
                delta = (delta_values.sum(axis=1)) ** 0.5

                # Extract labels
                labels = sheet_data.iloc[:, 0]

                # Create a DataFrame for the calculation results
                output_data = {
                    "Label": labels,
                    "Δδ": delta
                }
                output_df = pd.DataFrame(output_data)

                # Add the calculation results to the results dictionary
                output_dfs[sheet_name] = output_df

            # Save the calculation results of each group to separate Excel files
            for group_name, output_df in output_dfs.items():
                output_file = os.path.join(output_folder, f"{group_name}_output.xlsx")
                output_df.to_excel(output_file, index=False)
                print(f" '{group_name}' is output to {output_file}")


input_folder = "CSP_input"
output_folder = "CSP_output"
calculate_delta(input_folder, output_folder)