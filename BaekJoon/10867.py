N=int(input())
j=list(set(list(map(int,input().split(" ")))))
j.sort()
for k in j:
    print(k,end=" ")
