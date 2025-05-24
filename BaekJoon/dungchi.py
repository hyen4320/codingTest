import sys

input=sys.stdin.readline

N=int(input())
race=[]
li=[]
ranking_li=[1 for i in range(N)]
for i in range(0,N):
    n1=list(map(int,input().split()))
    li.append(n1)

for j in range(N):
    for k in range(0,N,1):
        if(li[j][0]<li[k][0] and li[j][1]<li[k][1]):
            ranking_li[j]=ranking_li[j]+1
for e in ranking_li:
    print(e,end=" ")