from flask import Flask, render_template, send_from_directory, request
import util
import os
import socket


app = Flask(__name__)

app_path = os.path.dirname(os.path.abspath(__file__))

@app.route('/api/analyze_file/<filename>')
def analyze_file_code_convention(filename=''):
    '''
    This RESTful API analyze file
    '''
    # TODO!!!!!!
    if util.get_file_extension(filename) == 'py':
        log_path = util.py_file_code_convention_analysis('test.py')
        fp_log = open(log_path, 'r')
        content = fp_log.read()
        fp_log.close()
        return content

@app.route('/api/analyze_code/<code_type>', methods=['POST','GET'])
def analyze_code(code_type='py'):
    '''
    This RESTful API analyze upload code
    '''
    if code_type == 'py':
        # Post code
        if request.method == 'POST':
            filename = 'database/current.py'
            fp = open(filename, "w")
            fp.write(request.form['code'])
            fp.close()
            return 'Success'
        # Analysis and GET reviews
        if request.method == 'GET':
            filename = 'current.py'
            reviews = util.py_file_code_convention_analysis(filename)
            return reviews
    if code_type == 'java':
        # Post code
        if request.method == 'POST':
            filename = 'database/current.java'
            fp = open(filename, "w")
            fp.write(request.form['code'])
            fp.close()
            return 'Success'
        # Analysis and GET reviews
        if request.method == 'GET':
            filename = 'current.java'
            reviews = util.py_file_code_convention_analysis(filename)
            return reviews


@app.route('/')
def index():
    # test tmp
    # log = util.py_file_code_convention_analysis('test.py')
    log = 'Reviews will be displayed here.'
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
    app.debug = True
    # get current machine IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    app.run(host=ip)

# app.run(host='150.216.56.49')
