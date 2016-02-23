def isPhoneNumber(text): #define a function named isPhoneNumber and pass it input of text
    if len(text) != 12: #if the length of the input does not equal 12, return boolean value False
        return False
    for i in range(0,3): #for the number of iterations, stored in variable i, called for in the range function(in this case: 0,1,2)
        if not text[i].isdecimal(): #if the text character at index [substitute variable i] is not an integer, return boolean value False
            return False
    if text[3] != '-': #if the text character at index 3 does not equal a hypen, return boolean value False
        return False
    for i in range(4,7): #for the number of iterations, stored in variable i, called for in the range function (in this case: 4,5,6)
        if not text[i].isdecimal(): #if the text character at index [substitute variable i] is not an integer, return boolean value False
            return False
    if text[7] != '-': #if the text character at index 7 does not equal a hypen, return boolean value False
        return False
    for i in range(8,12): #for the number of iterations, stored in variable i, called for in the range function (in this case: 8,9,10,11)
        if not text[i].isdecimal(): #if the text character at index [substitute variable i] is not an integer, return boolean value False
            return False
    return True #otherwise, return boolean value True

'''
print('415-555-4242 is a phone number:') #print the text displayed inside the single quotes
print(isPhoneNumber('415-555-4242')) #call the function defined above and pass it the text string in parantheses for evaluation
print('Moshi moshi is a phone number:')#print the text displayed inside the single quotes
print(isPhoneNumber('Moshi moshi'))#call the function defined above and pass it the text string in parantheses for evaluation
'''

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)): #for the number of iterations, stored in variable i, called for in the range function (in this case, the length [number of characters] in the variable message)
    chunk = message[i:i+12] #create new variable, chunk, with the value of the idices of the variable message for the slice between i and i+12
    if isPhoneNumber(chunk): #if by calling the function isPhoneNumber and passing it the variable chunk returns True
        print('Phone number found: ' + chunk) #print string plus the variable chunk
print('Done') #once the message has been evaluated, print Done
