import json
from datetime import datetime, timedelta
from random import shuffle

def parse_team(query_result):
	'''
	this function jsonifies team query results
	'''
	result_list = []
	for element in query_result:
		result_list.append({'team_name': element.name, 'id': element.id})
	# print({'all_teams':result_list})
	return json.dumps({'all_teams':result_list})


def schedule(query_result, start_time1, start_time2, max_team_num, presentation_time):
	'''
	this function will schedule the team presentation 
	'''
	result_list = []
	for element in query_result:
		result_list.append({'team_name': element.name, 'id': element.id})
	# randomly shuffle the team order
	# arrary of dictionary [{},{},...]
	shuffle(result_list)

	# TODO check if number of team is less than max_team_num
	# first day schedule
	first_day = []
	cur_time = start_time1
	for i in range(max_team_num):
		# json cannot handle time directly
		first_day.append({'team':result_list[i], 'start_time': str(cur_time)})
		cur_time = cur_time + timedelta(minutes=presentation_time)
		# first_day is an array of dictionary [{'team':{'team_name': element.name, 'id': element.id}}, ...]

	# second day schedule
	second_day = []
	cur_time = start_time2
	left_team = len(result_list) - max_team_num
	for i in range(left_team):
		second_day.append({'team':result_list[i+max_team_num], 'start_time': str(cur_time)})
		cur_time = cur_time + timedelta(minutes=presentation_time)

	return json.dumps({'first_day':first_day, 'second_day':second_day})