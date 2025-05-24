import math

n,m,k=map(int,input().split(" "))
a=0.0
j=0
for i in range(k+1,1,-1):
    
    a+=i/n-j
    j+=1
    print(a)
print(a)