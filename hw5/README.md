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
- Create a web app including backendand and frontend to show user survey results using tables
- Choose any database (such as PostgreSQL and sqlalchemy) you like to store [user survey data](data/we_are_not_alone_no_nan.csv).
- Retrieve user suvey data from your database and split data into groups
	- Step 1, split data based on age and gender
		- Group 1: young (<=35) male
		- Group 2: middle-aged or old (>=36) male
		- Group 3: young (<=35) female
		- Group 2: middle-aged or old (>=36) female
	- Step 2, split data groups generated from Step 1 into based smaller groups based on countries, such as US groups and Canada groups.
	- Step 3, check which groups from Step 2 have more than 10 elements. If yes, use KMeans (check util.cluster_user_data and util.split_user_data) to split them into subgroups.
- Visualize all the groups with tables on the frontend (check sample code in hw5)


