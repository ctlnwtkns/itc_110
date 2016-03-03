'''
Write a function that takes a string and does the same thing as the strip()
string method (remove whitespace characters, i.e. space, tab, newline). 

If no arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. 

Otherwise, the characters specified in the second argument
to the function will be removed from the string.
'''

import re

def v(str, sub = None):	
	if sub != None:
		regex = re.compile(sub)
		mo = regex.search(str)
		strip = re.sub(mo.group(),'', str)
		print(strip)
	else:
		regexString = re.compile(r'\S.*\S', re.I|re.DOTALL)
		mo = regexString.search(str)
		print(mo.group())

v('			hello world', 'orld')


