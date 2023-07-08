import json
from tarfile import data_filter
from flask import Flask, request
import pandas as pd
from flask import send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/aboutus')
def aboutUs():
    return 'this is about us page'

@app.route('/course', methods=['POST'])
def contactUs():
    return 'this is contact us page'#9508038514

@app.route('/json-to-csv', methods=['POST'])
def json_to_csv():
    json_data = request.get_json()
    json_string = json.dumps(json_data)
    df = pd.read_json(json_string)
    df.index = pd.RangeIndex(start=1, stop=len(df)+1)
    df.to_csv('output.csv', index_label='SR NO.')
    #df.to_csv('output1.csv', index=True)
    return send_file('output1.csv', as_attachment=True)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username == 'prashant' and password == 'prashant123':
        return 'Login successful'
    else:
        return 'Incorrect credentials'
if __name__ == '__main__':
    app.run(port=3000, debug=True)