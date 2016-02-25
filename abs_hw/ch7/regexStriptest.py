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

def regexStrip(str):
	regexString = re.compile(r'\S.*\S', re.I|re.DOTALL)
	mo = regexString.search(str)
	print(mo.group())

str = '			hello world'
regexStrip(str)	

'''

import re

# An example string.
v = "running eating reading"

# Replace words starting with "r" and ending in "ing"
# ... with a new string.
v = re.sub(r"r.*?ing", "ring", v)
print(v)

Output

ring eating ring

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

v('		hello world', 'orld')


import re

def v(str, sub = None): 
	#compile whole string
	if sub != None:
		regex = re.compile(sub) #compile the string to be removed
		mo = regex.search(str) #create match object by searching for 
		#remove 'orld'
		v1 = regex.sub('', mo.group(), 1) #replace mo with blank space
		print(v1)
	else:
		str = re.compile(r'\S.*\S', re.I|re.DOTALL)
		mo = str.search(v)
		print(mo.group())
v('hello world', 'orld')


'''
'''
print'Type something: '
mnstr = raw_input()#.decode('string-escape')
print'Type something else, or hit enter: '
substr = raw_input()#.decode('string-escape')

v(mnstr, substr)
'''
'''