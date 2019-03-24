import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import util

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)

class Role(db.Model):
	# __tablename__ class variable defines the name of the table in the database
	__tablename__ = 'roles'
	# first column is named 'id'
	# possible second parameters:
	# primary_key If set to True , the column is the table’s primary key
	# unique If set to True , do not allow duplicate values for this column
	# index If set to True , create an index for this column, so that queries are more efficient
	# nullable If set to True , allow empty values for this column. If set to False , the column will not allow null values
	# default Define a default value for the column
	id = db.Column(db.Integer, primary_key=True)
	# second column is named 'name'
	name = db.Column(db.String(64), unique=True)
	# define defines the reverse direction of the relationship, by adding a role attribute to the User model
	# This attribute can be used on any instance of User instead of the role_id foreign key to access the Role model as an object.
	users = db.relationship('User', backref='role')
	# give them a readable string representation that can be used for debugging and testing purposes
	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	# The role_id column added to the User model is defined as a foreign key
	# roles.id refers to roles -> id column
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	def __repr__(self):
		return '<User %r>' % self.username

@app.route('/')
def index():
	# locates all the subclasses of db.Model and creates corresponding tables in the database for them
	# brute-force solution to avoid updating existing database tables to a different schema
	db.drop_all()
	db.create_all()
	# insert rows
	admin_role = Role(name='Admin')
	mod_role = Role(name='Moderator')
	user_role = Role(name='User')
	user_john = User(username='john', role=admin_role)
	user_susan = User(username='susan', role=user_role)
	user_david = User(username='david', role=user_role)
	# since now admin_role.id will be none because the changes are not committed
	# commit changes:
	db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
	db.session.commit()
	return render_template('index.html', log_html=User.query.all())

# default page for 404 error
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404_error.html'), 404

# default page for 500 error
@app.errorhandler(500)
def server_error(e):
	print(e)
	return render_template('500_error.html'), 500

@app.route('/test_500')
def fake_function():
	'''
	Need to test this wehn debug mode is off
	'''
	a = v * 5
	return a

if __name__ == '__main__':
	# app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)

