#https://www.codingame.com/ide/puzzle/horse-racing-duals

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

list = []
list1 = []
n = int(input())
list.append(n)
for i in range(n):
    pi = int(input())
    list.append(pi)
list.sort(reverse = True)
listnum = len(list)

for j in range(listnum - 1):
    rstnum = list[j] - list[j+1]
    j = j +1
    list1.append(rstnum)

list1.sort()


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(list1[0])
