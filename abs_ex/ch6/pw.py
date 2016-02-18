#! /usr/bin/env python3
# pw.py - an insecure password locker program

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6', 'luggage':  '12345'}
	
import sys
if len(sys.argv) < 2:
	print('Usage: python pw.py [acount] - copy account password')
	sys.exit()
	
account = sys.argv[1] #first command line arg is the account name

import pyperclip
if account in PASSWORDS:
	pypclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account + ' .')
	