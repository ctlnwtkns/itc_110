#! /usr/bin/env python3
# tablePrinter.py - displays a list of values in a well-ordered table

tableData = [['apples', 'oranges', 'cherries', 'bananas'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidth = [0] * len(tableData)
    for n in range(0,3):
        colWidth[n] = ((max(len(i) for i in tableData[n])))
    for j in range(0,4):
        print(tableData[0][j].rjust(colWidth[0]), ' ',
              tableData[1][j].rjust(colWidth[1]), ' ',
              tableData[2][j].rjust(colWidth[2]), ' '
              )

printTable()
