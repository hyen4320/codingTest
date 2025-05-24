N=int(input())

for i in range(N):
    count=0
    x=input()
    y=input()
    for i in range(len(x)):
        if(x[i]!=y[i]):
            count+=1
        
    print(f"Hamming distance is {count}")
