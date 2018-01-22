from flask import Flask, request, render_template from casuserutil import Casuserutil from urlparameterhandleutil import Urlparameterhandleutil

app = Flask(name)

@app.route('/', methods=['GET']) def login(): return render_template('login.html')

@app.route('/login', methods=['POST']) def handleLoginForm(): username = request.form['username'] password = request.form['password'] casuserutil = Casuserutil() result = casuserutil.verify_login_user(username, password) if result==0: return render_template('index.html', username=username) return render_template('login.html', message='Bad username or password', username=username)

@app.route('/exit', methods=['GET']) def exit(): return render_template('login.html')

@app.route('/bubblesort', methods=['GET']) def bubbleSort(): parameters = request.query_string urlparameterhandleutil = Urlparameterhandleutil() beforeSortData = parameters afterSortData = urlparameterhandleutil.analyze_url_paramters(beforeSortData.decode()) beforeSortData = afterSortData return render_template('bubble-sort.html', beforeSortData=beforeSortData, afterSortData=afterSortData)

if name == 'main': app.run(host='10.10.163.15', port=5000)