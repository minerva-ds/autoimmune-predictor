import pandas as pd

# Define the path to the medical conditions data file
mcq_file_path = 'P_MCQ.XPT'

# Load the medical conditions data
mcq_data = pd.read_sas(mcq_file_path, format='xport')

# Print the first few rows to verify the data
print(mcq_data.head())

# Check for specific columns related to autoimmune diseases
print(mcq_data.columns)

print(mcq_data.info())
