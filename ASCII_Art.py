#https://www.codingame.com/ide/puzzle/ascii-art

import sys
import math

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list10 = []
lindex = []
alist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?','!']

l = int(input()) #4
h = int(input()) #5
t = input()#MANHATTAN
uppert1 = t.upper()
uppert2 = uppert1.replace("@","?")
tlist = list(uppert2)
#print(tlist)
number = len(tlist)

for i in range(0,number):
    lindex.append(alist.index(tlist[i]))

#print(lindex)

letter1 = input()
letter2 = input()
letter3 = input()
letter4 = input()
letter5 = input()

for i in range(0,l*26):
    list10.append(i * l)

for i in list10:
    list1.append(letter1[i:i+l])

for i in list10:
    list2.append(letter2[i:i+l])

for i in list10:
    list3.append(letter3[i:i+l])

for i in list10:
    list4.append(letter4[i:i+l])

for i in list10:
    list5.append(letter5[i:i+l])

#print(lindex)
for i in range(0,number):
    print(list1[lindex[i]], end='',flush=True)

print('')

for i in range(0,number):
    print(list2[lindex[i]], end='',flush=True)

print('')

for i in range(0,number):
    print(list3[lindex[i]], end='',flush=True)

print('')

for i in range(0,number):
    print(list4[lindex[i]], end='',flush=True)

print('')

for i in range(0,number):
    print(list5[lindex[i]], end='',flush=True)
