from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import requests,uuid, os, json
from datetime import datetime
import random
import pandas as pd
import string
from flask_cors import CORS, cross_origin
from flask_session import Session

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = "AufarsFunProject"


@app.route('/')
@cross_origin()
def index():
	return render_template('tes_control2.html')

if __name__ == '__main__':
	app.run(debug=True)