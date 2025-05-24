import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=[input().rstrip("\n") for _ in range(a+b)]
d=set(c)
for j in d:
    c.remove(j)
print(len(c))
for _ in c:
    print(_)
