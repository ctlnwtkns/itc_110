import re #import the regex module

def joke():
	print 'knock knock'
	response = raw_input()
	'''answerRegex = re.compile(r'[W|w]ho[s|(\')?](\w)? [T|t]he(i)?r(e)?(\?)*')'''
	answerRegex = re.compile(r'who[s|(\')?](\w)? the(i)?r(e)?(\?)*', re.I)
	mo = answerRegex.search(response)
	if mo != None:
		if response in mo.group():
			print('To.')
			response2 = raw_input()
			answerRegex2 = re.compile(r'to who(\?)*', re.I)
			mo2 = answerRegex2.search(response2)
			if response2 in mo2.group():
				print('To WHOM.')
			
		
joke()
        


'''
else:
			print('Ugh! Seriously? Try again.')
			joke()
	else:else: 
			print('Don\'t you know how this works? Try again.')
    		joke()

		
    	'''