N=int(input())

li=list(map(int, input().split()))
li2=list(map(int,input().split()))
ans_li=[]

li.sort()
for j in range(0,N,1):
    elemt=li[0]
    big_num=0
    for i in range(0,len(li2),1):
        if li2[i] > big_num:
            big_num=li2[i]
    ans_li.append(big_num*elemt)
    del li[li.index(elemt)]
    del li2[li2.index(big_num)]
print(sum(ans_li))


