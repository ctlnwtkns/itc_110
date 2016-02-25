'''
How would you write a regex that matches the full name of someone whose last name is Nakamoto?

You can assume that the first name that comes before it will always be one word that begins with a capital letter.


* The regex must match the following:  
    -'Satoshi Nakamoto'
    - 'Alice Nakamoto'
    - 'Robocop Nakamoto'
  
* but not the following:  
    -'satoshi Nakamoto' (where the first name is not capitalized)
    -'Mr. Nakamoto' (where the preceding word has a non-letter character)
    -'Nakamoto' (which has no first name)
    -'Satoshi nakamoto' (where Nakamoto is not capitalized)

'''
import re

def Nakamoto():
	print('What is your name?')
	name = raw_input()
	nameRegex = re.compile(r'[A-Z][a-z]+\sNakamoto')
	mo = nameRegex.search(name)
	if mo != None:
		print('Hello ' + name)
	else:
		print('access denied')
		Nakamoto()

Nakamoto()
		