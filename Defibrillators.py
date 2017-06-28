#https://www.codingame.com/ide/puzzle/defibrillators

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
list = []
list2 = []
lonlist = []
latlist = []
namelist = []
lonip = input()#3.87
latip = input()#43.60
distancecal = []
resdissort = []
lon = lonip.replace(",",".")
lat = latip.replace(",",".")

n = int(input())#3,167
for i in range(n):
    a = input()
    dot = a.replace(",",".")
    b = dot.split(';')
    list.append(b)


for i in range(n):
    d = list[i]
    list2 = d[1:]
    namelist.append(list2[0])
    lonlist.append(list2[3])
    latlist.append(list2[4])

for i in range(n):
    cal = (float(lat) + float(latlist[i]))/2
    cal2 = math.radians(cal)
    cos = math.acos(cal2)
    x = (float(lonlist[i]) - float(lon)) * float(cos)
    y = (float(latlist[i]) - float(lat))
    distance = math.sqrt(x**2 * y**2) * 6371
    distancecal.append(distance)


resdissort = distancecal.copy()#base = resdissort, resdis ->sorted one
distancecal.sort()
#print (lon,lat)
#print (distancecal)
#print (resdissort)
number = resdissort.index(distancecal[0])
#print (number)
final = namelist[number]
#print (distancecal[36],distancecal[73])
print(final)
