#Automate the Boring Stuff with Python pp. 77

def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = (number // 2)
        else:
            number = (3 * number +1)
        print(number)

print('Enter a number.')
number = int(input())
collatz(number)
