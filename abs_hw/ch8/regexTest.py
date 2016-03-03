import re

print('Type first and last name:')
name = raw_input()
readRegex = re.compile(r'(\s)?\w*\s\w*', re.I)
mo = readRegex.search(name)
if mo != None:
	print(name)