def spam():
    print(eggs)  #ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()

#1. global variable eggs set to equal value 'global'
#2. spam function called
#3. spam function defined
#4. print function calls argument eggs
#5. returns error
