from itertools import combinations
def gcd(a,b):
    while b!=0:
        a,b = b , a%b
    return a

N = int(input())
for i in range(N):
    b=[]
    sum=0
    a=list(map(int,input().split(" ")))
    b=a[1::]
    b=list(combinations(b,2))
    for j in b:
        k,l=j[0],j[1]
        sum+=gcd(l,k)
    print(sum)
# print(b)        
# print(g)