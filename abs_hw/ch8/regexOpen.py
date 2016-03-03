#! /usr/bin/env python3
#regexOpen.py - a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints results to screen


import re, os

def search(name):
#list all files in current working directory
	pwd = os.getcwd()
	contents = os.listdir(pwd)
	txtRegex = re.compile(r'.*.txt$')
#open all .txt files
	for i in contents[:]:
		mo = txtRegex.search(i)
		if mo != None:
			search = os.path.join(pwd, i)
			openFile = open(search)
			readFile = openFile.read()
			
			#regex to search for (anything)
			readRegex = re.compile(r'.*')

			#search input for match object and store in mo variable
			mo = readRegex.search(readFile)

			#evaluate match object and print results
			if mo != None:
				print('Hello ' + name)
			else:
				print('Name not found.')
'''
			readRegex = re.compile(r'^Name:(/s)?[a-z].*/s[a-z].*/n', re.I)
			mo = readRegex.search(readFile)
			if mo == name:
				print(os.path.basename(search))
'''		

#receive user-supplied phrase			
print('Please type your first and last name:')
name = raw_input()


		
'''		
r'[a-z](/w)*/s[a-z](/w)*', re.I	
		for n in search[:]:
			
			readRegex = re.compile(r'^Name:[A-Z].*/s[A-Z].*/n/n')
			mo = readRegex.search(readFile)
			if mo != None:
				print(read(readFile))
			
'''		

'''
#regex to open files with student name
(r'^Name:(/s)?[a-z].*/s[a-z].*/n/n', re.I)

#regex to search for files that begin with 'Name:'
(r'^Name:')




'''
