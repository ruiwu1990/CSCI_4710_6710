# example is based on http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import util

# get current app directory
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/data/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# request.file <class 'werkzeug.datastructures.FileStorage'>
		# request.url is http://127.0.0.1:5000/
		# check if the post request has the file part
		if 'file' not in request.files:
			log = 'no file field in request.'
			return render_template('fail.html', log = log)
		# print(request.files['file'])
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			log = 'Empty filename.'
			return render_template('fail.html', log = log)
		if file and util.allowed_file(file.filename):
			# get filename in a safe way
			filename = secure_filename(file.filename)
			# check if the data folder exists, if not create one
			if os.path.exists(app.config['UPLOAD_FOLDER']) == False:
				os.makedirs(app.config['UPLOAD_FOLDER'])
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return render_template('success.html',filename=filename)
	elif request.method == 'GET':
		return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)

