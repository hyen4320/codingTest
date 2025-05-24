# from itertools import combinations

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

N=int(input())
b=[_ for _ in range(1,N+1,1)]
count=0
for x in b:
    if(N<x):
        if gcd(x,N)==1:count+=1
    else:
        if gcd(N,x)==1:count+=1
print(count)

#https://m.blog.naver.com/yyhjin12/222864062441
