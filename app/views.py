from flask import render_template,flash,redirect
from app import app 
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Miguel' } # fake user
	posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    	]
	return render_template("index.html", title = 'nihao', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form=form, providers = app.config['OPENID_PROVIDERS'])

@app.route('/echar_test')
def echar_test():
	timeData = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
	data1=[0,23416,0,0,7464,0,0,27216,0,2336,16240,3360,18432,20656,11848,4896,7464,2560,12744,2560,4608,512,14064,11776]
	data2=[0,23416,0,0,7464,0,0,27216,0,2336,16240,3360,18432,20656,11848,4896,7464,2560,12744,2560,4608,512,14064,11776]
	return render_template("echar_test.html",timeData=timeData, date1='201004', date2='201005', data1=data1,data2=data2)

@app.route('/echarts.min.js')
def echar_js():
	return render_template("echarts.min.js")
