import random

guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again.')
	guesss = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
	
'''
line 6 --> line 3 --> NameError --> must enter "'heads'" or "'tails'" 
line 8 --> "toss" (which will only ever be 0 or 1) can never equal "guess" (which should be "heads" or "tails"); the comment needs to be translated into code
line 12 --> misspelled guess(s)
'''