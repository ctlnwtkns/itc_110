def spam(divideBy):
    return 42 / divideBy
    
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))  #jumps to except clause and keeps going
    print(spam(1))
except ZeroDivisionError:
        print('Error: Invalid argument.')


#1. call function print with argument spam of parameter 2
#2. returns 21.0
#3. call function print with argument spam of parameter 12
#4. returns 3.5
#5. call function print with argument spam of parameter 0
#6. encounters ZeroDivisionError
#7. prints new error message
#8. return newline of value None
#9. call function print with argument spam of parameter 1
#10. returns 42.0

