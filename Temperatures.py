#https://www.codingame.com/ide/puzzle/temperatures
import sys
import math

temps = []
#pluses = []
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input().split() # the n temperatures expressed as integers ranging from -273 to 5526
#results = list(map(int, results))

temps = list(map(int,temps)) #받은 값을 int로 바꿈
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# math.abs(-1) => 1
# abs, min, max
# res

if n == 0: # 조건 비교시엔,== 대입시엔 =
    res = 0
else:
    res = temps[0]

for i in range(1, n): # 0부터 시작하는데, 1부터 시작함. 자기자신과의 비교는 안하기 위해서
    if abs(res) > abs(temps[i]): # res > temps[i]는 할 필요가 없어서 if문을 타지 않음
        res = temps[i]
    elif abs(res) == abs(temps[i]):
        res = max(res, temps[i])

print(res)

'''
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
'''
