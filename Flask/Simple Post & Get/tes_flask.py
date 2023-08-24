from flask import Flask, request

app = Flask(__name__)

@app.route('/tes', methods=['GET'])
def hello():
    return {'test_key' : "test_value"}

@app.route('/trade_detail', methods=['POST'])
def trade_detail():
    try:
        trade_id = int(request.form['trade_number'])
    except:
        return {"Error Message" : "Please input the right trade number."}
    
    return {"id" : trade_id}

print("App Name :", __name__)

if __name__ == '__main__':
    app.run(debug=True, port=5000)