HW5

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

TODO!!!!! TELL US HOW TO SETUP YOUR DATABASE HERE STEP BY STEP

Then you can start the server with:
```
python3 main.py
```

### Data
Survey data can be found at <mark>data/we_are_not_alone_no_nan.csv</mark>, -1 is used to represent NAN (i.e. missing data)

If your data is stored in sqlalchemy and want to output data as a python dictionary, here is [a possible solution](https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict).

### Requirements
If less than 10 answers, place in one table without clustering
