import random

'''
guess = '' #create an empty global guess variable
while guess not in ('heads', 'tails'): #check whether the local guess variable equals either 'heads' or 'tails'; if not, continue printing prompt
	print('Guess the coin toss! Enter heads or tails:')
	guess = raw_input()
toss = random.randint(0,1) # 0 is tails, 1 is heads #create toss variable and set it equal to either 0 or 1
if toss == guess: # check whether the value of toss (either 0 or 1) equals the value of guess (the local variable); if yes, print 'You got it!'
	print('You got it!')
else:
	print('Nope! Guess again.') #if no, print 'Nope! Guess again.'
	guesss = raw_input() #and reset local guess variable to equal new user input
	if toss == guess: #reevaluate whether toss equals guess
		print('You got it!') #if yes, print 'You got it!'
	else: #if no, print 'Nope....'
		print('Nope. You are really bad at this game.')


line 6 --> line 3 --> NameError --> input() won't accept value...needs to be updated to raw_input
line 8 --> "toss" (which will only ever be 0 or 1) can never equal "guess" (which should be "heads" or "tails"); the comment needs to be translated into code
line 12 --> misspelled guess(s)
'''

guess = ''
while guess not in ('heads', 'tails'): 
	print('Guess the coin toss! Enter heads or tails:')
	guess = raw_input()
toss = random.randint(0,1) 
if toss == guess: 
	print('You got it!')
else:
	print('Nope! Guess again.') 
	guesss = raw_input() 
	if toss == guess: 
		print('You got it!') 
	else: 
		print('Nope. You are really bad at this game.')