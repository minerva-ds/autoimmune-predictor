import pandas as pd
import requests
from io import BytesIO

# Define URLs for the necessary files
file_urls = {
    'demographic': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT',
    'dietary_day1': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR1TOT_J.XPT',
    'dietary_day2': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR2TOT_J.XPT',
    'medical_conditions': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/MCQ_J.XPT',
    'laboratory_data': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BPX_J.XPT',
}

# Function to download and load XPT files
def download_and_load_xpt(url):
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_sas(BytesIO(response.content), format='xport')

# Download and load the files into DataFrames
data_frames = {name: download_and_load_xpt(url) for name, url in file_urls.items()}

# Filter relevant columns from each DataFrame
demographic_cols = ['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'DMDEDUC2', 'INDHHIN2']
dietary_cols = ['SEQN', 'DR1TKCAL', 'DR1TCARB', 'DR1TPROT', 'DR1TFAT']
medical_conditions_cols = ['SEQN', 'MCQ010', 'MCQ053', 'MCQ080', 'MCQ160A', 'MCQ160B', 'MCQ160C', 'MCQ160D', 'MCQ160E', 'MCQ160F', 'MCQ220']
laboratory_cols = ['SEQN', 'BPXSY1', 'BPXDI1', 'LBXTC', 'LBXLDL', 'LBXHDL', 'LBXGLU', 'LBDGLUSI', 'LBXCRP']

# Filter columns
data_frames['demographic'] = data_frames['demographic'][demographic_cols]
data_frames['dietary_day1'] = data_frames['dietary_day1'][dietary_cols]
data_frames['dietary_day2'] = data_frames['dietary_day2'][dietary_cols]
data_frames['medical_conditions'] = data_frames['medical_conditions'][medical_conditions_cols]
data_frames['laboratory_data'] = data_frames['laboratory_data'][laboratory_cols]

# Merge the DataFrames on SEQN column
merged_data = data_frames['demographic']
for key in ['dietary_day1', 'dietary_day2', 'medical_conditions', 'laboratory_data']:
    merged_data = merged_data.merge(data_frames[key], on='SEQN', how='inner')

# Display the first few rows of the merged data
print(merged_data.head())

# Display the number of rows in the merged data
print(f"Number of rows in the merged data: {merged_data.shape[0]}")
