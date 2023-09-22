## You are a Site Reliability Engineer, and you have a giant pile of logs to look through.
## We need to know what the most frequent error is, and what kinds of errors there are, and under what HTTP response code they will fall

raw_logs = """
[WARNING] 403 Forbidden: No token in request parameters
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
[WARNING] 403 Forbidden: No token in request parameters
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: Login Successful
[ERROR] 500 Server Error: int is not subscriptable
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
[WARNING] 403 Forbidden: No token in request parameters
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
[INFO] 200 OK: Login Successful
[INFO] 200 OK: User sent a message
[ERROR] 500 Server Error: int is not subscriptable
"""

## Write a function called analyze_logs that will accept logs as a string 

# Return a dictionary with logging statistics, that is formatted like so ( don't worry about spacing or formatting, only the data matters )


output = {
	'WARNING': {
		'403': {
			'Forbidden': {
				'No token in request parameters': 3
			}
		}
	},
	'ERROR': {
		'500': {
			'Server Error': {
				'int is not subscriptable': 8
			}
		}
	},
	'INFO': {
		'200': {
			'OK': {
				'Login Successful': 6,
				'User sent a message': 6
			}
		}
	}
}

output["WARNING"]["403"]["Forbidden"]["No token in request parameters"] # 3

# When printed it will more likely look like this:
printed_output = {'WARNING': {'403': {'Forbidden': {'No token in request parameters': 3}}}, 'ERROR': {'500': {'Server Error': {'int is not subscriptable': 8}}}, 'INFO': {'200': {'OK': {'Login Successful': 6, 'User sent a message': 6}}}}