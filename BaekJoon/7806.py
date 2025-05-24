import sys
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def factorial(n):
    _ = [x for x in range(1,n+1)]
    sum=1
    for i in _:
        sum*=i
        
    return sum
def ertostenes(n):
    a=[False,False]+[True]*(n-1)
    primes=[]
    for i in range(2,n+1):
      if a[i]:
         primes.append(i)
         for j in range(2*i,n+1,i):
            a[j] = False
    return primes
input=sys.stdin.readline
a=True
while a:
    line=input()
    a= list(map(int,line.split(" "))) if line!="\n" else False
    if a==False:
        break
    print(gcd(factorial(ertostenes(a[0])[-1]),a[1]))
