from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read Table 1 data from CSV file
table1_data = pd.read_csv('Table_Imput.csv', index_col=0)

@app.route('/')
def display_tables():
    # Calculate values for Table 2
    alpha_value = table1_data.loc['A5', 'Value'] + table1_data.loc['A20', 'Value']
    beta_value = table1_data.loc['A15', 'Value'] / table1_data.loc['A7', 'Value']
    charlie_value = table1_data.loc['A13', 'Value'] * table1_data.loc['A12', 'Value']

    # Prepare Table 2 data
    table2_data = [
        {"Category": "Alpha", "Value": alpha_value},
        {"Category": "Beta", "Value": beta_value},
        {"Category": "Charlie", "Value": charlie_value}
    ]

    return render_template('tables.html', table1=table1_data, table2=table2_data)

if __name__ == '__main__':
    app.run()
