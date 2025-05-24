import math
N=int(input())
a=[]
for i in range(1,N+1,1):
    if N%i==0:
        a.append(i)
print((sum(a)*5)-24)