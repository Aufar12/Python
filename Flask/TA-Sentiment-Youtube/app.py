from flask import Flask, redirect, url_for, render_template, request, Response, jsonify
import time
import algorithms,scraping, preprocess
import numpy as np

app = Flask(__name__)

comments = []
label = []
cleanComment = []

decision_tree = []
gnb = []
knn = []
svm = []

matrixDT = []
matrixNB = []
matrixKNN = []
matrixSVM = []

search = ""

@app.route('/form', methods=["POST", "GET"])
def form():
    scraping.reset()
    if request.method == "POST":
        global search
        nama = request.form['nama']
        search = nama
        return redirect(url_for("user", name=nama))
    else:
        return render_template("form.html")

@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))

@app.route('/progress')
def progress():
    def generate():
        x = 0

        while x <= 100:
            yield "data:" + str(x) + "\n\n"
            x = x + 10
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')


@app.route('/<name>')
def user(name):
    return render_template("index.html", x=name, y = ["Decision Tree", "KNN", "Naive Bayes", "SVM"])

@app.route('/google')
def google():
    return redirect("http://www.google.com", code=302)

@app.route('/hello')
def hello():
    return render_template("index.html", x=comments)

@app.route('/tree')
def tree():
    global decision_tree, gnb, knn, svm, cleanComment, label, \
        matrixDT, matrixNB, matrixKNN, matrixSVM
    if(len(decision_tree) > 0):
        return redirect(url_for("chart", dt=decision_tree))
    else:
        if (len(cleanComment) > 0):
            dt, nb, knn, svm, matrixDT, matrixNB, matrixKNN, matrixSVM = algorithms.accuracy(cleanComment, label)
            decision_tree = [element * 100 for element in dt]
            decision_tree = np.around(decision_tree, decimals=2)
            gnb = [element * 100 for element in nb]
            gnb = np.around(gnb, decimals=2)
            knn = [element * 100 for element in knn]
            knn = np.around(knn, decimals=2)
            svm = [element * 100 for element in svm]
            svm = np.around(svm, decimals=2)

            return redirect(url_for("chart"))
        else:
            return redirect(url_for("calculate"))

@app.route('/cleanse')
def cleanse():
    global decision_tree, comments, label, cleanComment
    if(len(decision_tree) > 0):
        return redirect(url_for("chart"))
    else:
        if (len(comments) > 0):
            cleanComment, label = preprocess.cleanse(comments)
            return redirect(url_for("calculate"))
        else:
            return redirect(url_for("cleansing"))

@app.route('/scrap')
def scrap():
    global comments, cleanComment, label, decision_tree, gnb, knn, svm, matrixDT, matrixNB, matrixKNN, matrixSVM
    result = scraping.scrap(search)
    comments = []
    cleanComment, label, decision_tree, gnb, knn, svm, matrixDT, matrixNB, matrixKNN, matrixSVM \
        = [], [], [], [], [], [], [], [], [], []
    comments = result
    return redirect(url_for("preview"))


@app.route('/preview')
def preview():
    global comments
    jumlah = len(comments)+1
    return render_template("comments.html", x=comments, y=jumlah)
#=========================================================

from random import randint

@app.route('/_stuff')
def stuff():
    v = scraping.xc
    # return jsonify(result=time.time())
    return jsonify(result=v)


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    scraping.reset()
    if request.method == "POST":
        global search
        nama = request.form['nama']
        search = nama
        return redirect(url_for("scrap", name=nama))
    else:
        return render_template("scraping.html")


@app.route('/chart')
def chart():
    return render_template('chart.html', dt = decision_tree, nb = gnb, knn=knn, svm=svm,
                           mDT = matrixDT, mNB = matrixNB, mKNN = matrixKNN, mSVM = matrixSVM)

@app.route('/calculate')
def calculate():
    jumlah = len(cleanComment) + 1
    return render_template('calculate.html', y=jumlah)

@app.route('/cleansing')
def cleansing():
    jumlah = len(comments) + 1
    return render_template('preprocessing.html', y=jumlah)


if __name__ == '__main__':
    app.run()
