b=list(map(int,input().split(" ")))
check=b.index(1)
if(check==0):
    if b==[1,2,3,4,5,6,7,8]:
        print("ascending")
    else:
        print("mixed")
elif(check==7):
    if b==[8,7,6,5,4,3,2,1]:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")
