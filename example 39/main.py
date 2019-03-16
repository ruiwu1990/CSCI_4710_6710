from flask import Flask, render_template, jsonify, json
import time
import util


app = Flask(__name__)

@app.route('/api/random_number', methods=['GET'])
def api_random_num():
	'''
	RESTful API: generate a random number in a JSON file
	'''
	rand_num = util.random_int()
	tmp_name = 'random_number'
	json_dict = {
		'name': tmp_name,
		'number': rand_num
	}

	# convert dictionary to json obj
	json_obj = json.dumps(json_dict)
	return json_obj

@app.route('/api/random_number_complex', methods=['GET'])
def api_random_num_complex():
	'''
	RESTful API: generate a random number in a JSON file
	'''
	rand_num = util.random_int()
	tmp_name = 'random_number'
	json_dict = {
		'name': tmp_name,
		'number': rand_num
	}

	# convert dictionary to json obj
	json_obj = json.dumps(json_dict)
	# wait 1 second
	time.sleep(1)
	return json_obj

@app.route('/')
def index():
    # this is your index page
    log = 'Hello world.'
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

