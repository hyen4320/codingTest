import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
##uclid는 재귀 안 씀 
#def uclid(_n,_m):
#    if(_m==0):
#        return _n
#    return uclid(_m,_n%_m)
## 오버플로우 잡아야함
def uclid(a,b):
    while b!=0:#파이썬은 자동으로 큰 수 처리해줘서 오버플로우 걱정할 필요 없음
        a,b=b,a%b
    return a

N=input()
_=list(map(int,input().rstrip("\n").split(" ")))
n=1
m=1
for i in _:
    n*=i

M=int(input())
_=list(map(int,input().rstrip("\n").split(" ")))
for j in _:
    m*=j
if n<m:
    print(f"{str(uclid(m, n))}"[-9:])

else:
    print(f"{str(uclid(n, m))}"[-9:])
