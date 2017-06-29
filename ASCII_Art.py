#https://www.codingame.com/ide/puzzle/ascii-art

import sys
import math

alist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?' # 리스트가 아니라도 원하는 숫자를 꺼내 쓸 수 있음

width = int(input()) # L
height = int(input()) # H
txt = input() # N = len(txt), ex) E / MANHATTAN

for _ypos in range(height): # _pos를 타지 않음. 쓰지 않으니까 _를 앞에 붙임. _단독으로는 바로 전함수를 호출할 수 있어서 잘 쓰지 않음
    charset_oneline = input()#전체를 한줄에 받음

    line_output = ''

    for char in txt:
        char = char.upper()

        idx = alist.find(char)
        if idx == -1: #find에서 없으면 -1을 리턴함
            idx = alist.find('?')

        xpos = idx * width #알파벳 순서 * 넓이
        line_output += charset_oneline[ xpos : xpos+width ] #알파벳 넓이 시작부터 (:) 넓이만큼

    print(line_output)



func3(func2(func()))

'''
import sys
import math

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list10 = []
lindex = []
alist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'

l = int(input()) #4
h = int(input()) #5
t = input()#MANHATTAN
uppert_letter = t.upper()
replaced_uppert = uppert_letter.replace("@","?")
textlist = list(replaced_uppert) #alphabets order
#print(tlist)
number = len(textlist)

for i in range(0,number):
    lindex.append(alist.index(textlist[i]))

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


'''
