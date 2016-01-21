import random
spam = 0
while spam <= 10:
  spam = random.randint(1,12)
  if spam == 2:
    print('Howdy ' + str(spam))
  elif spam == 1:
    print('Hello ' + str(spam))
  elif spam > 2:
    print('Greetings! ' + str(spam))
