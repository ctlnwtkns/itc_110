###Practice Questions
####Why are functions advantageous to have in your programs?
Functions set apart blocks of code so that 1) you don't need to repeat yourself if parts of your program call for the same function, and 2) the function's code is isolated from the rest of the program, and thus easier to debug. 
####When does the code in a function execute: when the function is defined or when the function is called?
The code in a function executes when a funcion is called.
####What statement creates a function?
The `def` statement creates a function.
####What is the difference between a function and a function call?
A function is the code block following the `def` statement; and function call is the name of the function followed by a set of parentheses containing the parameters of the argument.
####How many global scopes are there in a Python program? How many local scopes?
There is only one global scope in a Python program and as many local scopes as there are functions defined. 
####What happens to variables when a function call returns?
Local variables do not persist outside of local scopes, so that when a function call returns, a local variable is effectively "forgotten."
####What is a return value? Can a return value be part of an expression?
A return value is whatever an expression evaluates down to. A return value can be specified within (as a part of) an expression.
####If a function does not have a return statement, what is the return value of a call to that function?
`None`
####How can you force a variable in a function to refer to the global variable?
You can force a variable in a function to refer to the global variable by typing `global <variable name>` at the beginning of the statement.
####What is the data type of `None`?
The data type of `None` is the None data type. 
####What does the `import areallyourpetsnamederic` statement do? 
This statement imports a module called areallyourpetsnamederic.
####If you had a function named `bacon()` in a module named `spam`, how would you call it after importing `spam`? 
`spam.bacon()`
####How can you prevent a program from crashing when it gets an error?
By using the try and except statements. 
####What goes in the `try` clause? What goes into the `except` clause?
Put the error-prone code into the `try` clause, and put whatever you want returned in the event of an error into the `except` clause. 

