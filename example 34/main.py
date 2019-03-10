from flask import Flask, render_template
import util


app = Flask(__name__)


@app.route('/')
def index():
    # this is your index page
    log = 'Hello world.'
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

