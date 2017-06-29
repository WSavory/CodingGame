#https://www.codingame.com/ide/puzzle/chuck-norris

import sys
import math

binlist = []
iplist = []
strlist = []
sec =''
message = str(input())
iplist = list(message)

for i in range(len(iplist)):
    strlist.append(str("{0:b}".format(ord(iplist[i]))))

#print(iplist)
#print(ord(message))
#print(str("{0:b}".format(ord(iplist[0]))))
#print(strlist)

for i in range(0,len(strlist)):
    if len(strlist[i]) == 6:
        strlist[i] = '0' + strlist[i]

#print(strlist)

ans = ''.join(strlist)

ans = ans.replace('10','1,0')
ans = ans.replace('01','0,1')
binlist.append(ans.split(','))
'''
for i in range(len(strlist)):
    strlist[i] = strlist[i].replace('10','1,0')
    strlist[i] = strlist[i].replace('01','0,1')
    binlist.append(strlist[i].split(','))
'''
#print(((binlist[0][0])[0]))
#print(binlist)

#for i in range(0,len(binlist)):
#    ans.append(str(binlist[0]))
    #ans = ''.join(binlist)#
#print(ans)

#list1 = ['1', '2', '3']
#str1 = ''.join(list1)


for i in range(0,len(binlist)): # one character :1 0000 11
    for j in range(0,len(binlist[0])): #1, 0000, 11
        if ((binlist[i][j])[0]) == '1':
            sec = sec + '0 '
            sec = sec + ('0' * len(binlist[i][j])) + ' '
            #print(i,j+j)
        elif ((binlist[i][j])[0]) == '0':
            sec = sec + '00 '
            sec = sec + ('0' * len(binlist[i][j])) + ' '
            #print(i,j)

        #sec = sec + ' '
        strsec = sec.strip()

print(strsec)









'''
list1 = []
list2 = []

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = str(input())
list1 = list(message) # ['c','c']
#splited = message.split(',')

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#answer = ord(message) # convert to ascii
for i in range(len(list1)):
    list1[i] = "{0:b}".format(ord(list1[i]))
    list1[i] = list1[i].replace('10','1,0')
    list1[i] = list1[i].replace('01','0,1')
    list1[i] = list1[i].split(',')
    #print(list1[i])

a = ''

#num = len(list1)
for k in range(len(list1)): # 0 1 2
    num = len(list1[k])
#    print(num)
    for i in range(0,num-1):
        for j in range(0,num-1):
            res = list1[i][j]
            if res == '1':
                a = a + ('0')
                a = a + (' ')
                a = a + ('0' * len(list1[i][j]))
                a = a + (' ')
            elif res == '0':
                a = a + ('00')
                a = a + (' ')
                a = a + ('0' * len(list1[i][j]))
                a = a + (' ')
a = a.strip()
#print(asc,"0 0 00 0000 0 00",file=sys.stderr)
#C = 100011, % = 101001
#print(asc)
print(list1)
print(a)
'''
