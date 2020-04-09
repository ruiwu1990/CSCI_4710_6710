from flask import Flask, render_template, jsonify, json
import util


app = Flask(__name__)

# 127.0.0.1:5000/api/random_number
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

# 127.0.0.1:5000/
@app.route('/')
def index():
    # this is your index page
    log = 'Hello world.'
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

