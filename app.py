from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_tables():
    # Read data from CSV file for Table 1
    df_table1 = pd.read_csv('Table_Input.csv')
    
    # Calculate Table 2 values
    alpha = df_table1.loc[df_table1['Index'] == 'A5', 'Value'].values[0] + df_table1.loc[df_table1['Index'] == 'A20', 'Value'].values[0]
    beta = df_table1.loc[df_table1['Index'] == 'A15', 'Value'].values[0] / df_table1.loc[df_table1['Index'] == 'A7', 'Value'].values[0]
    charlie = df_table1.loc[df_table1['Index'] == 'A13', 'Value'].values[0] * df_table1.loc[df_table1['Index'] == 'A12', 'Value'].values[0]
    
    # Prepare data for Table 2
    table2_data = [
        {'Category': 'Alpha', 'Value': alpha},
        {'Category': 'Beta', 'Value': beta},
        {'Category': 'Charlie', 'Value': charlie}
    ]
    
    # Render the HTML template with both tables
    return render_template('tables.html', table1=df_table1.to_dict('records'), table2=table2_data)

if __name__ == '__main__':
    app.run()

