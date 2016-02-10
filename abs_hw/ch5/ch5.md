### What does the code for an empty dictionary look like?
variable name, assignment operator, open/close curly brackets

`spam = {}`
###What does a dictionary value with a key 'foo' and a value 42 look like?
`{'foo':42}`

###What is the main difference between a dictionary and a list?
A dictionary is not ordered like a list. 

###What happens if you try to access spam['foo'] if spam is {'bar': 100}?
A `KeyError` is returned.

###If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

###If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

###What is a shortcut for the following code?
```python
if 'color' not in spam:
  spam['color'] = black
```

```python
spam.setdefault('color', 'black')
```

###What module and function can be used to “pretty print” dictionary values?
