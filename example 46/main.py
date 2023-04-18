from flask import Flask, render_template, jsonify
import pickle
import util


app = Flask(__name__)


@app.route('/')
def index():

    log = 'Hello world.'

    return render_template('index.html', log_html = log)


@app.route('/api/get_prediction/<input_X>', methods=['GET'])
def ml_prediction(input_X=''):
    # http://127.0.0.1:5000/api/get_prediction/0,0,1,0,0,0,0,0,11.27735924,0,1,13.35,0
    filename = 'ML/ML_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    # create string arrays
    input_X = input_X.split(",")
    # convert strings to numbers
    input_X = [float(i) for i in input_X]
    # input_X = [0, 0, 1, 0, 0, 0, 0, 0, 11.27735924, 0, 1, 13.35, 0]

    # Object of type ndarray is not JSON serializable
    pred = list(loaded_model.predict([input_X]))
    # jsonify returns js object
    return jsonify({'prediction': pred})

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

