import sys

input=sys.stdin.readline
li=[]
comp_sum=0
check=0
li=[int(input())for i in range(9)]
comp_sum=sum(li)-100
for j in range(0,9,1):
    if(check==1):
        break
    for k in range(j+1,9,1):
        if(li[j]+li[k]==comp_sum):
            li.remove(li[j])
            li.remove(li[k-1])
            check=1
            break
        else:
            pass
for item in li:
    print(item)
