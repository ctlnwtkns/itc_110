def spam():
    global eggs
    eggs = 'spam'  #this is the global

def bacon():
    eggs = 'bacon'  #this is the local

def ham():
    print(eggs)  #this is the global

eggs = 42  #this is the global
spam()
print(eggs)

#1. global variable eggs is set (eggs = 42)
#2. function spam() is called
#3. function spam() is defined
#4. global variable eggs is reset to = 'spam'
#5. print(eggs) returns 'spam'
