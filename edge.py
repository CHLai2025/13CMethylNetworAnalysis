import pandas as pd

excel_file_path = 'connection.xlsx'

# Read the Excel file and remove spaces from each cell.
df = pd.read_excel(excel_file_path)
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Extract the corresponding data from columns A and C
result = [(row['Label'], row['file']) for _, row in df.iterrows()]

print(result)