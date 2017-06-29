import sys
import math

list1 = []
list2 = []

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#answer = ord(message) # convert to ascii
asc = "{0:b}".format(ord(message))

a = asc.replace('10','1,0')
b = a.replace('01','0,1')

list2 = b.split(',')

for i in range(len(list2)):
    res = list2[i][0]
    if res == '1':
        print('0', end='',flush=True)
        print(' ', end='',flush=True)
        print('0' * len(list2[i]), end='',flush=True)
        print(' ', end='',flush=True)
    elif res == '0':
        print('00', end='',flush=True)
        print(' ', end='',flush=True)
        print('0' * len(list2[i]), end='',flush=True)
        print(' ', end='',flush=True)


#print(b,"0 0 00 0000 0 00",file=sys.stderr)

#print(list2)
