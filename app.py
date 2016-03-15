#!flask/bin/python
from flask import Flask, render_template, flash, redirect, json, Response, request, session
from flask.ext.sqlalchemy import SQLAlchemy #Using Database SQLite
from flask import render_template
from flask.ext.triangle import Triangle 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///member.db'
db = SQLAlchemy(app)
Triangle(app) 

class Member(db.Model): #database model for Member storage
	name = db.Column(db.Text, primary_key=True, index=True)
	phone = db.Column(db.Text)
	def __repr__(self):
		return '<Member %r>' % (self.name)
    	def __init__(self, phone, name):
    		self.phone = phone
    		self.name = name


def db_init():
        #if empty table   empty lists are false
	if not Member.query.all():
                db.create_all()
		m = Member(name="Tian", phone="6471891111")
		db.session.add(m)
		db.session.commit()

db_init()

@app.route('/') #renders the index.html file at the template directory
def index():
	return render_template('index.html',title='index')


@app.route('/members', methods=['GET'])
def return_members():
	members=Member.query.all()
	result_list=[]
	for member in members:
		result={}
		result['name']=member.name
		result['phone']=member.phone
		result_list.append(result)
	js = json.dumps(result_list)
	resp = Response(js, status=200, mimetype='application/json')
	resp.headers['Link']='localhost:5000'
	return resp

@app.route('/members/<string:cust_name>', methods=['GET'])
def return_member(cust_name):
	member=Member.query.filter_by(name=cust_name).first()
        result={}
	#validation
	if member is None:
		result['success']='false'
		result['error']='Member not in database'
	else:
		result['name']=member.name
		result['phone']=member.phone
		result['success']='true'
	js= json.dumps(result)
	resp = Response(js, status=200, mimetype='application/json')
	resp.headers['Link']='localhost:5000'
	return resp

@app.route('/members/add', methods=['POST','PUT'])
def add_member():
	content = request.get_json(silent=True)
        result={}
        #validation
	if('name' in content and 'phone' in content):
		try:
			member=Member(name=content['name'], phone=content['phone'])
			db.session.add(member)
			db.session.commit()
			result[content['name']]=content['phone']
			result['success']='true'

		except:
			result['error']='Duplicate Name'
			result['success']='false'
	else:
		result={}
		result['error']='Input json is not correct'
		result['success']='false'
	js= json.dumps(result)
	resp = Response(js, status=201, mimetype='application/json')
	resp.headers['Link']='localhost:5000'
	return resp




if __name__ == "__main__":
    app.run()
