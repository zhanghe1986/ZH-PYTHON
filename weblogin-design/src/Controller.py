from flask import Flask, request, render_template
from service.Casuserutil import *
from service.Urlparameterhandleutil import *

app = Flask(__name__)

casuserutil = Casuserutil()

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handleLoginForm():
    username = request.form['username']
    password = request.form['password']
    result = casuserutil.verify_login_user(username, password)
    if result==0:
        return render_template('index.html', username=username)
    #return render_template('login.html', message='Bad username or password', username=username)
    return render_template('register.html')
	
@app.route('/register', methods=['POST'])
def handleRegisterForm():
	username = request.form['username']
	password = request.form['password']
	casuserutil.save_user_info(username, password)
	return render_template('login.html')
    

@app.route('/exit', methods=['GET'])
def exit():
    return render_template('login.html')
	
@app.route('/bubblesort', methods=['GET'])
def bubbleSort():
    parameters = request.query_string
    urlparameterhandleutil = Urlparameterhandleutil()
    beforeSortData = parameters
    afterSortData = urlparameterhandleutil.analyze_url_paramters(beforeSortData.decode())
    beforeSortData = afterSortData
    return render_template('bubble-sort.html', beforeSortData=beforeSortData, afterSortData=afterSortData)

if __name__ == '__main__':
    app.run(host='ip', port=5000)