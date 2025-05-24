import sys
input=sys.stdin.readline
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
N=int(input().rstrip("\n"))

a=list(map(int,input().rstrip("\n").split(" ")))

