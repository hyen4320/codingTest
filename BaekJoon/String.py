# alpha_dict={("A","B","C"):3,
#             ("D","E","F"):4,
#             ("G","H","I"):5,
#             ("J","K","L"):6,
#             ("M","N","O"):7,
#             ("P","Q","R","S"):8,
#             ("T","U","V"):9,
#             ("W","X","Y","Z"):10}

# sum=0
# a=input()
# for i in a:
#     for key,value in alpha_dict.items():
#         if i in key:
#             sum+=value
# print(sum)

# a=int(input())
# for j in range(0,a):
#     print(" "*(a-j-1),end="")
#     print("*"*(j*2+1))

# for k in range(a-1,0,-1):
#     print(" "*(a-k),end="")
#     print("*"*(k*2-1))

# s=input()
# # print(len(s)//2)
# sum=0
# for i in s:
#     sum+=ord(i)
#     print(sum)
# for j in range(0,len(s)//2):
#     sum-=ord(s[j])*2
#     print(sum)
# if(sum==0):
#     print(1)
# elif(97<=sum<=122):
#     print(1)
# else:
#     print(0)

s=input()
check=False
for i in range(0,len(s)//2+1,1):
    # print(len(s)-i)
    # print(i)
    check=s[i]==s[len(s)-1-i]
if(check):
    print(1)
else:
    print(0)