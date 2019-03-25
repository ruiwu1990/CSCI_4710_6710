import os
from flask import Flask, request, render_template
import json
import util

# get current app directory
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + '/data/'

app = Flask(__name__)
app.config['DATA_FILE'] = UPLOAD_FOLDER + 'NRDC_data.csv'
# TODO, this should be dynamically obtained from your CSV file
# you can check how to do it with Example 38
app.config['COL_NAME'] = 'Temperature'

@app.route('/api/process_csv/<lower_threshold>/<upper_threshold>')
def process_csv(lower_threshold='', upper_threshold=''):
	qualified, outlier = util.threshold_process_method(app.config['DATA_FILE'], app.config['COL_NAME'], float(lower_threshold), float(upper_threshold))
	# print(qualified)
	return qualified

@app.route('/')
def index():
    # this is your index page
    log = 'Hello world.'
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

