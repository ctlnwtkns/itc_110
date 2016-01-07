##Practice Questions
###Which of the following are operators, and which are values?
|Symbol|Type
---|---
|*|operator
|'hello'|value
|88.8|value
|-|operator
|/|operator
|+|operator
|5|value

###Which of the following is a variable, and which is a string?

  spam —> variable 
  
  'spam' —> string

###Name three data types.

  float, string, integer
###What is an expression made up of? What do all expressions do?
An expression is made up of values and operators. All expressions reduce to a single value.
###This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
An expression performs more of an evaluative function, whereas a statement assumes a fixed value. 
###What does the variable bacon contain after the following code runs?
 bacon = 20
 
 bacon + 1
 
 21 
 
###What should the following two expressions evaluate to?
'spam' + 'spamspam'

‘spam spamspam’

'spam' * 3

‘spamspamspam’

###Why is eggs a valid variable name while 100 is invalid?
100 is an invalid variable name because the variable name cannot begin with a number. 
###What three functions can be used to get the integer, floating-point number, or string version of a value?
int(), float(), str()
###Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
The expression causes an error because the integer 99 cannot be concatenated to the strings ‘I have eaten’ and ‘burritos.’ In order to fix it, convert the integer to a string using the str() function. 
‘I have eaten ’ + str(99) + ‘ burritos.’

###Extra credit: 
Search online for the Python documentation for thelen() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.

 https://docs.python.org/3/library/functions.html

`print('Enter the radius to find the area of the circle:')`

`r = input()`

`circle = 3.14*int(r)**2`

`print(round(circle, 1))`





