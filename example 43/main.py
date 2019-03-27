import os
from flask import Flask, request, render_template
import json
import util

# get current app directory
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/data/'

app = Flask(__name__)
app.config['META_FILE'] = UPLOAD_FOLDER + 'meta_data.txt'


@app.route('/api/save', methods=['POST'])
def process_csv():
	input_values = request.form
	result_str = 'First Name:' + request.form['first_name'] + '\n' + \
				 'Last Name:' + request.form['last_name'] + '\n' + \
				 'Email:' + request.form['email']
	# print(result_str)
	text_file = open(app.config['META_FILE'], "w")
	text_file.write(result_str)
	text_file.close()
	return render_template('success.html')

@app.route('/')
def index():
    # this is your index page
    log = 'Hello world.'
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

