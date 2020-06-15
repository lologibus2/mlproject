from datetime import datetime

import pytz
from flask import Flask
from flask import request
from flask_cors import CORS
from termcolor import colored

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'OK'

@app.route('/print_name')
def print_name():
    return "My name is ada"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
