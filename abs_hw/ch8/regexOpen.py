#! /usr/bin/env python3
#regexOpen.py - a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints results to screen


import re, os

def search(name):
#list all files in current working directory 
	projectDir = '/Users/caitlin/Documents/school/itc_110/abs_ex/ch8/project1'
	os.chdir(projectDir)
	contents = os.listdir(os.getcwd())
	for i in contents[:]: #iterate through the indices of contents
		txtRegex = re.compile(r'.*.txt$')
		mo = txtRegex.search(i) #at each index, search for a match object 
		if mo != None: #if mo found	
			
			#open all .txt files
			openFile = open(i) #open file
			readFile = openFile.read() #read file
		
			#regex to search for (any quiz where name is not blank)
			readRegex = re.compile(r'Name:(\s)?[A-Z]([a-z])*\s[A-Z]([a-z])*', re.I)

			#search input for match object and store in mo variable
			mo = readRegex.search(readFile)

			#evaluate match object and print results (list of file names containing mo)
			if mo != None:
				#print(readFile)
				print(i)

#receive user-supplied phrase			
print('Please type your first and last name:')
name = raw_input()
search(name)

