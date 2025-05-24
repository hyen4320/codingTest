import math
N=int(input())
# def greedy()
for i in range(N):
    gloves=[]
    color, matches= map(int,input().split(" "))
    left=list(map(int,input().split(" ")))
    right=list(map(int,input().split(" ")))
    print(left)
    print(right)
    for i in range(len(left)):
        if left[i]-right[i]<0:
            gloves.append((left[i]-right[i])*-1)
        else:
            gloves.append(left[i]-right[i]) 
    print(gloves)
    print(sum(gloves))
    print(math.comb(sum(gloves),matches)/color)