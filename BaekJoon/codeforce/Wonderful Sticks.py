import random
N=int(input())
for i in range(N):
    a=[x for x in range(1,int(input())+1)]
    b=input()
    c=len(b)
    d=[]
    for j in range(len(b)):
        if(b[j]==">"):
            e=[x for x in a if x > max(d)]      
            # print(e)          
        else:
            e=[x for x in a if x < min(d)]
            # print(e)
        if e:
            print(e)
            f=random.choice(e)
            d.append(f)
            a.remove(f)
    print(*d)

    