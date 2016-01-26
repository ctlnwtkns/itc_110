#knock knock
#who's there?
#to.
#to who?
#to whom.

#import re
def joke():
    print('knock knock')
    response = input()
    if response == 'whos there?':  #find regular expression to capture all instances of who's there
        print('To.')
        response2 = input()
        if response2 == 'To who?':
            print('To WHOM.')
        else:
            print('Try again.')
            joke()

joke()

