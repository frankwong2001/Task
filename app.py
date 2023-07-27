import streamlit as st
import pandas as pd

# Read Table 1 from CSV file
table1_df = pd.read_csv('Table_Input.csv', index_col=0)

# Calculate values for Table 2
alpha_value = table1_df.loc['A5'] + table1_df.loc['A20']
beta_value = table1_df.loc['A15'] / table1_df.loc['A7']
charlie_value = table1_df.loc['A13'] * table1_df.loc['A12']

# Create DataFrame for Table 2
table2_df = pd.DataFrame({
    'Category': ['Alpha', 'Beta', 'Charlie'],
    'Value': [alpha_value.item(), beta_value.item(), charlie_value.item()]
})

# Create the Streamlit app
st.title('Table 1')
st.dataframe(table1_df)

st.title('Table 2')
st.dataframe(table2_df)
