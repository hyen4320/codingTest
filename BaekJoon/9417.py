from itertools import combinations
def gcd(a,b):
    while b!=0:
        a,b = b , a%b
    return a

N = int(input())
for i in range(N):
    sum=[]
    a=list(map(int,input().split(" ")))
    b=list(combinations(a,2))
    for j in b:
        k,l=j[0],j[1]
        sum.append(gcd(l,k))
    sum.sort(reverse=True)
    print(sum[0])