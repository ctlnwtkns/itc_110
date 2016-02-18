#! /usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points to start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes for lines listed
	lines[i] = '*' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)

