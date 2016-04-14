# -*- coding: utf-8 -*-
from app import db

#创建的 User 类包含一些字段，这些字段被定义成类的变量。字段是被作为 db.Column 类的实例创建的，db.Column 把字段的类型作为参数，并且还有一些其它可选的参数，比如表明字段是否唯一。
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	#__repr方法告诉python如何打印这个类的对象，可以用来调试
	def __repr__(self):
		return '<User %r>' % (self.nickname)
