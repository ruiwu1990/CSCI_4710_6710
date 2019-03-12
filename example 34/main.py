from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# 
app = Flask(__name__)

# route is used to map a URL with a Python function
@app.route('/')
# this is how you define a function in Python
def index():
    # this is your index page
    # no need to specify which type this varible is...
    # in Python you can even do this:
    # a = 'aaa'
    # a = 1
    log = 'Hello world.'
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

