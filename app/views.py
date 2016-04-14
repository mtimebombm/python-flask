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
	return render_template("echar_test.html")

@app.route('/echarts.min.js')
def echar_js():
	return render_template("echarts.min.js")
