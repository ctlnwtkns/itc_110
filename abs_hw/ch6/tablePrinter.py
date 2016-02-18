#! /usr/bin/env python3
# tablePrinter.py - displays a list of values in a well-ordered table

tableData = [['apples', 'oranges', 'cherries', 'bananas'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
'''	
def printTable(): 
	colWidth = [0] * len(tableData)
	for n in range(0,3):
# find longest value in each list in tableData and store value in colWidths[0]
		colWidth[n]=((max(len(i) for i in tableData[n])))
# print values from first list in tableData in column and right justify
	#for s in tableData[0]:
		#print(s.rjust(colWidth[0])) # for as many values as are in the first tableData array, then print each value
	print(0.rjust(colWidth[0]))
printTable()
'''

#print the first value from each list stored in tableData

for i in range(0,3):
	for j in range(0,3):
		print(i,' ',j,' ', tableData[i][j])


#for i, j in tableData[0][0]:
			