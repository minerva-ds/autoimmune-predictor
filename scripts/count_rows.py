import pandas as pd

# Load the XPT file (replace 'P_DR1TOT.XPT' with the actual file path)
file_path = 'P_DR1TOT.XPT'
dietary_data = pd.read_sas(file_path, format='xport')

# Explore the data
print(dietary_data.head())  # Display the first few rows
print(dietary_data.info())  # Display information about the dataset

# Check the number of rows
num_rows = len(dietary_data)
print(f'Number of rows in the dietary habits dataset: {num_rows}')
