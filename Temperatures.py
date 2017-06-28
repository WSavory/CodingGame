#https://www.codingame.com/ide/puzzle/temperatures

import sys
import math

temps = []
pluses = []
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input().split() # the n temperatures expressed as integers ranging from -273 to 5526
#results = list(map(int, results))

temps = list(map(int,temps))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


for i in range(0,n):
    if temps[i] < 0:
        pluses.append(temps[i] * -1) # convert negative
    else:
        pluses.append(temps[i])     # not convert

temps.sort()
pluses.sort()

if n == 0:
    temps.append(0) # 06 result
else:
    a = int(pluses[0]) * -1 # 02



if n-1 > 0:
    if temps[n-1] > 0:
        print (pluses[0])
    else:
        print(a)
else: #temps[0] = None:
    print(0)

#print(temps1[0])
#print(a)
#print(temps)
#print(pluses)
