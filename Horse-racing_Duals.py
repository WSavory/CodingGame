#https://www.codingame.com/ide/puzzle/horse-racing-duals
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

list = []
list1 = []

n = int(input())

for i in range(n):
    list.append(int(input()))

list.sort(reverse = True)

for j in range(len(list) - 1):
    rstnum = list[j] - list[j+1]
    j = j +1
    list1.append(rstnum)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min(list1))
