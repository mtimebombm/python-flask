from flask import render_template,flash,redirect,url_for
from app import app 
from .forms import LoginForm,IpForm

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


@app.route('/echar_test/<ip>')
def echar_test(ip):
	data={
		'info':[201004,201005],
		'timeData':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
		'data':[[0,23416,0,0,7464,0,0,27216,0,2336,16240,3360,18432,20656,11848,4896,7464,2560,12744,2560,4608,512,14064,11776],
				[0,416,0,0,764,0,0,2216,0,236,1640,360,1832,2066,1848,496,746,256,1244,256,468,52,1464,1776]],
		'info2':[1,2],
		'data2':[2000,8000]
	}
	return render_template("echar_test.html",data=data, ip=ip)

@app.route('/echarts.min.js')
@app.route('/echar_test/echarts.min.js')
def echar_js():
	return render_template("echarts.min.js")
	
@app.route('/echar_test', methods = ['GET', 'POST'])
def ip_input():
	form = IpForm()
	if form.validate_on_submit():
		return redirect(url_for('echar_test', ip=form.ip.data))
	return render_template('input_ip.html', title = 'Sign In', form=form, providers = app.config['OPENID_PROVIDERS'])
