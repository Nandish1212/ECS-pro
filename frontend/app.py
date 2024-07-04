from flask import Flask, render_template, request
import requests
import os

Backend_url = os.getenv('Backend_url', 'http://127.0.0.1:8000')
app = Flask(__name__)

@app.route('/')
def home():
    return 'Enter into the form!'

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    response=requests.post(Backend_url+'/submit' , json=form_data)
    return 'submitted'

@app.route('/get_data')
def get_data():
    response = requests.get(Backend_url + '/view')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
