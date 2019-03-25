import pandas as pd

def threshold_process_method(filename, col_name, lower_threshold, upper_threshold):
	'''
	this function will process a csv file and find values that are more than
	upper threshold or less than lower threshold
	'''
	df = pd.read_csv(filename)
	df_upper = df[df[col_name]>=lower_threshold]
	df_qualified = df_upper[df_upper[col_name]<=upper_threshold]

	df_outlier1 = df[df[col_name]<lower_threshold]
	df_outlier2 = df[df[col_name]>upper_threshold]
	# first is within thresholds, second is outlier df
	return df_qualified.to_dict(), pd.concat([df_outlier1, df_outlier2]).to_dict()