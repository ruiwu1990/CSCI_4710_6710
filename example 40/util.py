import json

def parse_user(query_result):
	'''
	this function jsonifies user query results
	'''
	result_list = []
	for element in query_result:
		result_list.append({'username': element.username, 'role_id': element.role_id})
	
	return json.dumps({'all_user':result_list})