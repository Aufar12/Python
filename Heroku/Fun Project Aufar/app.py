from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import requests,uuid, os, json
from datetime import datetime
import random
import pandas as pd
import string
from flask_session import Session

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
app.config['SECRET_KEY'] = "AufarsFunProject"

def read_excel():
	###
	data_notes  = pd.read_excel('notes.xlsx', sheet_name='Notes').values.tolist()
	return data_notes

data_all = read_excel()

@app.route('/')
def index():
	return redirect(url_for('notes'))

@app.route('/notes')
def notes():
	return render_template('./notes.html', data = data_all)


@app.route('/covid')
def covid():
	responseToday = requests.get("https://data.covid19.go.id/public/api/update.json")
	responseIndo = requests.get("https://api.kawalcorona.com/indonesia")
	responseJkt = requests.get("https://data.covid19.go.id/public/api/prov.json")
	return render_template('./covid.html', today = responseToday.json()['update']['penambahan'], jkt = responseJkt.json()['list_data'][0], indo = responseIndo.json()[0])

if __name__ == '__main__':
	app.run(debug=True)