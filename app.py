import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

@app.route('/')
def display_table1():
    # Read data from table1.csv
    data = read_csv_file('https://raw.githubusercontent.com/frankwong2001/Task/main/Table_Input.csv')
    return render_template('tables.html', data=data)

@app.route('/table2-data')
def get_table2_data():
    # Read data from table1.csv
    data = read_csv_file('https://raw.githubusercontent.com/frankwong2001/Task/main/Table_Input.csv')
    
    # Calculate Table 2 values
    a5_value = int(data[4]['Value'])
    a20_value = int(data[19]['Value'])
    alpha_value = a5_value + a20_value

    a15_value = int(data[14]['Value'])
    a7_value = int(data[6]['Value'])
    beta_value = a15_value / a7_value

    a13_value = int(data[12]['Value'])
    a12_value = int(data[11]['Value'])
    charlie_value = a13_value * a12_value

    table2_data = {
        'Alpha': alpha_value,
        'Beta': beta_value,
        'Charlie': charlie_value
    }

    return jsonify(table2_data)

if __name__ == '__main__':
    app.run()
