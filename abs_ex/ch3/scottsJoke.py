import sys
import random

def joke():
   while True:
       print("Knock knock")
       response = input()

       if response == "who's there":
           r = random.randint(1,3)
           if r == 1:
               print("Jehovah's Whitness.")
           elif r == 2:
               print("The Church of Jesus Christ of Latter-day Saints.")
           elif r == 3:
               print("The Catholic Church.")
           break
       else:
           print('You suck.')
           continue
       
joke()

#1. call function joke()
#2. define function joke()
#3. initiate infinite while loop
#4. print 'Knock knock'
#5. set variable response to user input value
#6. if variable response equals user input value 'who's there', then
#7. set variable r to a random integer value between 1 and 3
#8. if variable r equals 1,
#9. print 'Jehovah's witness'
#10. else if variable r equals 2,
#11. print 'The Church...'
#12. else if variable r = 3,
#13. print 'The Catholic Church'
#14. if neither 1, 2, nor 3, break
#15. and print 'You suck.'
#16. Then return to print 'Knock knock'
#17. and reset variable response as user input value
#18. and reevaulate response. 
