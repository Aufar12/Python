from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import requests,uuid, os, json
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random
import string
from flask_session import Session
import numpy as np
import pandas as pd
import pickle

clf_entropy = pickle.load(open("dectreemodel_entropy","rb"))

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
app.config['SECRET_KEY'] = 'redsfsfsfsfis'
curdir, data_all, session_holder = os.getcwd(), '', {}

def prediction(X_test, clf_object):
	y_pred = clf_object.predict(X_test)
	return y_pred.tolist()

def makepred(list):
	list2 = [list[1],list[4],list[6],list[7],list[8],list[11]]
	subjectpred = []
	subjectpred.append(list2)
	testdata = np.array(subjectpred)
	result = prediction(testdata,clf_entropy)
	return result[0]

def read_excel():
	data_pg  = pd.read_excel('questions.xlsx', sheet_name='PG').values.tolist()
	data_essay = pd.read_excel('questions.xlsx', sheet_name='Essay').values.tolist()
	data_all = data_pg + data_essay
	return data_all

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
def index():
	global data_all
	session_generator = id_generator()
	data_all = read_excel()
	return render_template('./start.html', session_id = session_generator)

@app.route('/choice/<int:page>/<string:session_id>', methods = ['GET','POST'])
def choice(page, session_id):
	global session_holder

	if request.method == 'POST' and page == 12:
		value = request.form['name_hidden_form']
		session['answers'+str(page)] = value
		page += 1
		return redirect(url_for('essay', page=page, session_id=session_id))
	elif request.method == 'POST':
		value = request.form['name_hidden_form']
		session['answers'+str(page)] = value
		page += 1
		return redirect(url_for('choice', page=page, session_id=session_id))
	else:
		return render_template('./choice.html', page=page, data=data_all[page-1])

@app.route('/essay/<int:page>/<string:session_id>',  methods = ['GET','POST'])
def essay(page, session_id):
	global session_holder

	if request.method == 'POST' and page == 17:
		value = request.form['name_hidden_form']
		session['answers'+str(page)] = value

		page += 1

		return redirect(url_for('result', session_id=session_id))
	elif request.method == 'POST':
		value = request.form['name_hidden_form']
		session['answers'+str(page)] = value
		page += 1

		return redirect(url_for('essay', page=page, session_id=session_id))
	else:
		return render_template('./essay.html', page=page,  data=data_all[page-1])

@app.route('/result/<string:session_id>')
def result(session_id):
	
	all_answer = []
	print('------------- SESSION --------------------')
	for i in range(1, 18):
		print(session['answers'+str(i)])
		all_answer.append(session['answers'+str(i)])
	print('------------- SESSION --------------------')


	x = makepred(all_answer)

	if 'Auf' in x :
		img_path = 'https://i.ibb.co/q5P1NLN/aufar.jpg'
	elif 'Mei' in x :
		img_path = "https://i.ibb.co/Z2LScFP/meilisa.jpg"
	elif 'rum' in x :
		img_path = "https://i.ibb.co/xDPCghm/arum.jpg"
	elif 'Yog' in x :
		img_path = "https://i.ibb.co/fqc3J45/yogie.jpg"
	elif 'Ris' in x:
		img_path = "https://i.ibb.co/h70YP2Z/riska.jpg"
	else:
		img_path = "Not Found"

	return render_template('./result.html', session_id=session_id, name=x, img_path = img_path)


@app.route('/generate/<string:session_id>/<string:person>')
def generate(session_id, person):

	questions, answers = [], []

	for i in data_all:
		questions.append(i[0])

	questions.append('Apakah benar orangnya?')

	for i in range(1, 18):
		answers.append(session['answers'+str(i)])

	answers.append(person)

	save_to_excel(session_id, questions, answers)
	return redirect(url_for('index'))

def save_to_excel(session_id, questions, answers):

	data = {'Questions': questions, 'Answers': answers}  
	df = pd.DataFrame(data)  

	now = datetime.now()
	dt_string = now.strftime("%d %B %Y %H;%M;%S")
	filename = dt_string +' - ID; '+ session_id + '.xlsx'

	with pd.ExcelWriter(filename) as writer:    
		df.to_excel(writer, 'Result')     
		writer.save()    

	sendEmail('Jawaban Questionaire - ' + session_id, attachments=[filename])
	os.remove(filename)

def sendEmail(message, types='text', attachments=[]):
    msg = MIMEMultipart()
    with open('email.json') as json_file:
        confMail = json.load(json_file)
    
    msg['From']     = confMail['displayname']
    msg['To']       = 'm.aufar12@gmail.com'
    msg['CC']       = 'm.aufar08@gmail.com'
    msg['Subject']  = '1st Anniversary PKC Questionaire'
    text = message

    if types=='html':
        msg.attach(MIMEText(text, 'html'))
    else:
        msg.attach(MIMEText(text, 'plain'))

    recipients = str(msg['To'] +', '+msg['CC']).split(', ')
    
    for f in attachments:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)
    
    server = smtplib.SMTP(confMail['server'], 587)
    server.starttls()
    server.login(confMail['email'], confMail['password'])
    server.sendmail(confMail['email'], recipients, msg.as_string())
    server.quit()

if __name__ == '__main__':
	app.run(debug=True)