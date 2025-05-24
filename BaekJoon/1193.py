from itertools import product
N=int(input())
result=[]
count=0
data=list(product(range(1,N+1),range(1,N+1)))
for i in range(N):
    result.append(list(data[i*N:(i+1)*N//2]))

for j in range(0,N):
    for k in range(0,j+1):
        count+=1
        if(count==N):
            answer=result[j][k]
            #print(answer)
        
print(str(answer[0])+'/'+str(answer[1]))