from flask import Flask, render_template
import util


app = Flask(__name__)

@app.route('/')
def index():
    log = 'Hello world.'
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

