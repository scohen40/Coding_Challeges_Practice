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

#assuptions
#- each log is ended by a newline character
def analyze_logs(logsString):
    logsMap = {}
    
    #split the string into individual logs by splitting by line breaks
    logs = logsString.split('\n')
    # print(logs)
    #loop through each log, find the log type, then the log code, then the log title, and finally the log message
    for log in logs[1:len(logs)-1]:
        
        #split each log into individual tokens/words by the spaces
        log = log.split()
        #get the log type
        logType = log[0].strip('[]')
        #get the log code
        logCode = log[1]
        #get the log title
        logTitle = ''
        #keep adding to the title if there's no ':'
        currentIndex = 2
        for word in log[2:]:
            currentIndex += 1 #increment for the next loop
            #add the word to the logTitle
            if ':' in word:
                logTitle += word.strip(':')
                break
            else:
                logTitle += word + ' '
        #get the log message
        logMessage = ' '.join(log[currentIndex:])

        #find/add all of that to the logsMap and add 1 to the count at that spot
        ## TO DO : SPLIT THE FOLLOWING STATEMENT UP TO ADD EACH PIECE TO THE MAP INDIVIDUALLY, DOING IT ALL TOGETHER DOESN'T WORK
        ## 1.5 hours until here
        logsMap[logType][logCode][logTitle][logMessage] = logsMap.get(logType, logCode).get(logCode, logTitle).get(logTitle, logMessage).get(logMessage, 0) + 1

    return logsMap

print(analyze_logs(raw_logs))