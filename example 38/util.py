import pandas as pd

# if a file extension is not listed, the system will not upload the file
ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preview_csv(filename):
	'''
	this function will return a JSON file
	containing the first 5 lines of a CSV file
	'''
	# read csv file
	# dataframe
	df = pd.read_csv(filename)
	# this will return the total length of your CSV file
	total_len = len(df)
	csv_values = []
	# if length is less than 5
	if total_len < 5:
		csv_values = df.values.tolist()
	else:
		csv_values = df.head(n=5).values.tolist()

	# grad column names
	col_names = df.columns.tolist()
	return col_names, csv_values