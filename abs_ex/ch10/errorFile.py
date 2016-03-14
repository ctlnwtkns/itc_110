'print traceback error message to log file'
'ABS p.218'

import traceback
try:
	raise Exception('This is an error message.')
except:
	errorFile = open('errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to errorInfo.txt')