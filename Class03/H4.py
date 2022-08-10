
#第一題
n=int(input())
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n-i):
        print( "*", end=" ")
    print()

#第二題
n=int(input())
for i in range(n):
    for j in range(n-i):
        print( " ", end=" ")
    for k in range(i+1):
        print( "*", end=" ")
    print()

#第三題

import math
matrix= [[],[]]
matrix[0] = list(map(int, input("point1:").split()))
matrix[1]  = list(map(int, input("point2:").split()))
dist = [0 for i in range(2)]
for i in range(2):
    for j in range(2):
        dist[i]= int(matrix[j][i])-dist[i]
print(dist)
print(math.sqrt(dist[0]**2+dist[1]**2))

#第四題

from random import randint
row=int(input("row:"))
col=int(input("col:"))
A = [[randint(1, 20) for y in range(col)] for x in range(row)]
print(A)
