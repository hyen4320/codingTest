N=int(input())
data=list(input().split(" "))

dot=[1,1]

move={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}

for i in data:
    x,y=move[i]
    print(x,y)
    dot[0]+=x
    dot[1]+=y
    if(dot[0]<=0 or dot[1]<=0 or dot[0]>N or dot[1]>N):
        dot[0]-=x
        dot[1]-=y
    print(dot)
print(dot)