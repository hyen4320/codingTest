m=input()
i,j=ord(m[0])-96,m[1]
print(i,j)
count=0
route=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
for row,column in route:
    if(i+row>0 and int(j)+column>0 and i+row<=8 and int(j)+column<=8):
        count+=1
    # print(row,column)
print(count)
