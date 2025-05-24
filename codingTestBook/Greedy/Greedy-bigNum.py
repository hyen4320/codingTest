N,M,K = map(int,input().split(" "))
li=list(map(int,input().split(" ")))
li.sort()
result=0
for i in range(1,M+1):
    if i%K==0:
        result+=li[-2]
    else:
        result+=li[-1]      
print(result)