import re #import the regex module

def joke():
    print('knock knock')
    response = re.compile(input()) #create a regex object with the re.compile() function. Remember to use a raw string
    print(response)
    mo = response.search('Who\'s there?') #pass the desired string into the regex object's search() method. This returns a Match object
    print('match object = ' + str(mo)) # call the Match object's group() method to return a string of the actual matched text
    
    '''if mo:
        print('To.')
        response2 = re.compile(input())
        if response2 == response.search('To who?'):
            print('To WHOM.')
        else:
            print('Try again.')
            joke()'''

joke()
        
