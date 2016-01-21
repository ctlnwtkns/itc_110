##Practice Questions

###What are the two values of the Boolean data type? How do you write them?
True and False (capitalize the first letters of each and forget the '').

###What are the three Boolean operators?
and, or, not

###Write out the truth tables of each Boolean operator.
**and**

|Expression|Evaluates to...|
|---|---|
True and True | True
True and False | False
False and True | False
False and False | False

**or**

|Expression|Evaluates to...|
|---|---|
True or True | True
True or False | True
False or True | True
False or False |False

**not**

|Expression|Evaluates to...|
|---|---|
not True | False
not False | True

###What do the follow expressions evaluate to?

|Expression|Evaluates to...|
|---|---|
`(5>4) and (3==5)` | False
`not (5>4)` | False
`(5>4) or (3==5)` | True
`not ((5>4) or (3==5))` | False
`(True and True) and (True == False)` | False
`(not False) or (not True)` | True

###What are the six comparison operators?
|Operator|Value|
|---|---|
== | equals
!=  | not equals
< | less than
> | greater than
<= | less than or equal to
>= | greather than or equal to

###What is the difference between the equal to operator and the assignment operator?
The *equal to* operator is two equal signs (==); the *assignment* operator is one equal sign (=)

###Explain what a condition is and where you would use one?
A condition is an expression (followed by a clause) which always evaluates down to either True or False and is used in a flow control statement such as *if*, *else*, and *elif*.

###Identify the three blocks in this code:

```python
spam = 0
if spam == 10:
  print('eggs') #block
  if spam > 5:
     print('bacon') #block
  else:
    print('ham') #block
  print('spam')
print('spam')
```

###Write code that prints `Hello` if 1 is stored in `spam`, prints `Howdy` if 2 is stored in `spam`, and prints `Greetings!` if anything else is stored in `spam`.

```python
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
```


###What can you press if your program is stuck in an infinite loop?
ctrl + c

###What is the difference between `break` and `continue`?
A `break` in the `while` loop's clause will immediately break the program out of the loop. A `continue` will cause the program to immediately jump back to the beginning of the clause and reevaluate from there. 

###What is the difference between `range(10)`, `range(0,10)`, and `range(0,10,1)` in a `for` loop?
`range(10)` means that the expression will be evaluated 10 times

`range(0,10)` means that the expression will be evaluated 10 times, beginning at 0 and ending at 9.

`range(0,10,1)` means that the expression will be evaluated 10 times, beginning at 0 and ending at 9, increasing at an interval of 1

###Write a short program that prints the numbers `1` and `10` using a `for` loop. Then write an equivalent program that prints the numbers `1` to `10` using a `while` loop. 

```python
for i in range(10):
  print(i)
```
```python
i = 0
while i < 10:
    print(i)
    i = i + 1
```

###If you had a function named `bacon()` inside a module named `spam`, how would you call it aftering importing `spam`?
`spam.bacon()`

###Extra Credit: Look up the `round()` and `abs()` functions on the Internet, and find out what they do. Experiment with them in the interactive shell. 
  
