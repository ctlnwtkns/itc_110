####What is [ ]?
The empty brackets represent a list value (specifically, an empty list value).
####How would you assign the value `hello` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains [2,4,6,8,10]).
`spam[3] = 'hello'`
####*For the following three questions, let’s say `spam` contains the list `['a','b', 'c', 'd']`.*
####What does `spam[int('3'*2)/11]` evaluate to?
A TypeError.
####What does `spam[-1]` evaluate to?
`'d'`
####What does `spam[:2]` evaluate to?
`['a', 'b']`
####*For the following three questions, let's say `bacon` contains the list [3.14, 'cat', 11, 'cat', True]*
####What does `bacon.index('cat')` evaluate to?
1
####What does `bacon.append(99)` make the list value in bacon look like?
`[3.14, 'cat', 11, 'cat', True, 99]`
####What does bacon.remove('cat') make the list value in bacon look like?
`[3.14, 11, 'cat', True, 99]`
####What are the operators for list concatenation and list replication?
`+`, `*`
####What is the difference between the append() and insert() list methods?
`append()` will add the new list value to the end of the existing list; insert() will insert the value at the specified index.
####What are two ways to remove values from a list?
One way is to use the `del` statement; another is to use the `remove()` method.
####Name a few ways that list values are similar to string values.
You can use the `len()` function; the `+` and `*`, `in` and `not in`, and augmented assignment operators; `for` loops; and indexing and slicing with both list values and string values. Also, both lists and strings are ordered sequences of values. 
####What is the difference between lists and tuples?
A list is a mutable data type; a tuple is an immutable form of a list data type. A list is invoked with square brackets`[ ]`; a tuple, with parenthese `( )`. 
####How do you type the tuple value that has just the integer value 42 in it?
`type((42,))`
####How can you get the tuple form of a list value? How can you get the list form of a tuple value?
`tuple()` and `list()`, respectively
####Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
These variables contain a list *reference*, or a value that points to the list. 
####What is the difference between copy.copy() and copy.deepcopy()?
`copy.copy()` makes a duplicate copy of the list; `copy.deepcopy()` will also make copies of the lists of the list.


