import os
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import json, util
from datetime import datetime 

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

class Team(db.Model):
	__tablename__ = 'team'
	# default Define a default value for the column
	id = db.Column(db.Integer, primary_key=True)
	# second column is named 'name'
	name = db.Column(db.String(64), unique=True)
	team_members = db.relationship('Team_member', backref='role')
	# give them a readable string representation that can be used for debugging and testing purposes
	def __repr__(self):
		return '<Team %r>' % self.name

# Not used in this application
class Team_member(db.Model):
	__tablename__ = 'team_member'
	id = db.Column(db.Integer, primary_key=True)
	team_member_name = db.Column(db.String(64), unique=True, index=True)
	team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
	def __repr__(self):
		return '<Team Member Name %r>' % self.team_member_name

@app.route('/')
def index():
	# locates all the subclasses of db.Model and creates corresponding tables in the database for them
	# brute-force solution to avoid updating existing database tables to a different schema
	db.drop_all()
	db.create_all()
	# insert rows
	team1 = Team(name='Team1')
	team2 = Team(name='Team2')
	team3 = Team(name='Team3')
	team4 = Team(name='Team4')
	team5 = Team(name='Team5')
	team6 = Team(name='Team6')
	team7 = Team(name='Team7')
	team8 = Team(name='Team8')
	team9 = Team(name='Team9')
	team10 = Team(name='Team10')
	team11 = Team(name='Team11')
	team12 = Team(name='Team12')
	team13 = Team(name='Team13')
	team14 = Team(name='Team14')
	team15 = Team(name='Team15')
	team16 = Team(name='Team16')
	team17 = Team(name='Team17')
	team18_1 = Team(name='Team18_1')
	team18_2 = Team(name='Team18_2')
	g_team1 = Team(name='g_Team1')
	g_team2 = Team(name='g_Team2')
	g_team3 = Team(name='g_Team3')
	g_team4 = Team(name='g_Team4')
	g_team5 = Team(name='g_Team5')
	# commit changes:
	db.session.add_all([team1, team2, team3, team4, team5, team6, team7, team8,
						team9, team10, team11, team12, team13, team14, team15, 
						team16, team17, team18_1, team18_2, g_team1, g_team2, 
						g_team3, g_team4, g_team5])
	db.session.commit()

	log = 'this app can generate team presentation order!'
	return render_template('index.html', log_html=log)


@app.route('/api/get_team', methods=['GET'])
def get_team():
	# print(Team.query.all())
	return util.parse_team(Team.query.all())

@app.route('/api/generate_presentation_order', methods=['GET'])
def random_order_team():
	return util.schedule(Team.query.all(), datetime(2020, 4, 23, 18, 00), datetime(2020, 4, 28, 18, 00), 12, 6)


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
	app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)

