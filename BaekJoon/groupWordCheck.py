a=int(input())
result=0
for i in range(0,a):
    s=input()
    li=[]
    dis=[]
    li=[s[x] for x in range(0,len(s))]

    # print(li)

    for j in li:

        dis.append(list(filter(lambda x: li[x] == j, range(len(li)))))
        
    for k in dis:
        
        if(len(k)==1 ):
            sdfsdf=""
        
        result+=1
print(result)
    # print(dis)
# print(result)

