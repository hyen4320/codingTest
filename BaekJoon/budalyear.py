# input()
# # c=list(map(int,input().split(" ")))[1]
# a=list(map(int,input().split(" ")))
# # b=int(input())
# # print(a.count(b))
# # count=[]
# # for i in a:
# #     if(i<c):
# #         count.append(i)
# # for j in count:
# #     print(j,end=" ")
# a.sort()
# print(a[0],a[-1])
# a=[]
# b=[]
# for i in range(0,9):
#     a.append(int(input()))
# b=a.copy()
# a.sort()
# print(a[-1])
# print(b.index(a[-1])+1)

# a,b=map(int,input().split(" "))
# c=[0 for x in range(a)]
# for i in range(b):
#     d,e,f=map(int,input().split(" "))
#     for j in range(d-1,e):
#         c[j]=f
# for k in c:
#     print(k,end=" ")

# a,b=map(int,input().split(" "))
# c=[x for x in range(1,a+1)]
# for i in range(b):
#     d,e=map(int,input().split(" "))
#     num=0
#     num=c[d-1]
#     c[d-1]=c[e-1]
#     c[e-1]=num
    
# for k in c:
#     print(k,end=" ")
# b=[]
# for i in range(10):
#     a=int(input())%42
#     b.append(a)
# print(len(set(b)))


# a,b=map(int,input().split(" "))
# v=[]
# c=[x for x in range(1,a+1)]
# for i in range(b):
#     d,e=map(int,input().split(" "))
#     v=c[d-1:e]
#     v.reverse()
#     c[d-1:e]=v
# for j in c:
#     print(j,end=" ")

# a=input()
# b=list(map(int,input().split(" ")))
# b.sort()
# c=[]

# for i in b:
#     c.append(i/b[-1]*100)

# print(float(sum(c))/float(len(c)))

# a=int(input())
# for i in range(a):
#     b=input()
#     print(b[0]+b[-1])

# a=list(input().strip().split(" "))
# if(a[0]==""):
#     print(0)
# else:
#     print(len(a))

# a=list(input().split(" "))

# if(int(a[0][::-1])<int(a[1][::-1])):
#     print(a[1][::-1])
# else:
#     print(a[0][::-1])

# import string
# a=input()
# b=[]
# alp=string.ascii_uppercase
# for i in range(len(a)):
#     if(15<=alp.index(a[i])<=18):
#         b.append(7)
#     elif(21<=alp.index(a[i])<=24):
#         b.append(9)
#     else:
#         b.append((alp.index(a[i])//3)+3)
#     #pqrs, wxyz는 4개임
# print(sum(b))
# import sys

# n=[]

# while True:
#     try:
#         a=input()
#         n.append(a)
#         if (a==""):
#             break
#     except EOFError:
#         break

# for i in n:
#     print(i)

# print("         ,r\'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")
# print(a)

# aa=[]
# bb=[]
# grade_num={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0,"P":False}
# for i in range(20):
#     a=list(input().split(" "))
#     if(a[2][0:2]=="P"):
#         continue
#     bb.append(float(a[1][0]))
#     aa.append(float(a[1][0])*grade_num.get(a[2][0:2]))
# if(sum(bb)==0):
#     bb.append(1.0)
# print(f"{sum(aa)/sum(bb):06f}")
# N,M=map(int,input().split(" "))
# a=[list(map(int,input().split(" "))) for _ in range(N)]
# b=[list(map(int,input().split(" "))) for _ in range(N)]

# for i in range(N):
#     for j in range(M):
#         print(a[i][j]+b[i][j],end=" ")
#     print()
# N=int(input())
# a=[[0]*100]*100
# for _ in range(N):
#     i,j=map(int,input().split(" "))
#     for k in range(i,i+10):
#         a[k][j]=1
#         for z in range(j,j+10):
#             a[k][z]=1
# # print(sum(a.count(1)))
# print(sum(row.count(1) for row in a))

# a,b=input().split(" ")
# result=0
# B=int(b)
# A=len(a)
# for i in range(len(a)):
#     num=ord(a[i])
#     if(num<60):
#         result+=int(a[i])*(B**(A-i-1))
#     else:
#         result+=(num-55)*(B**(A-i-1))
# print(result)

# import math
# a,b,v=map(int,input().split())
# n=((v-a)/(a-b))+1
# print(math.ceil(n))

# x,y,w,h=map(int,input().split(" "))
# a=[x,y,w-x,h-y]
# print(min(a))

# a=input()
# l=len(a)
# check=True
# for i in range(int(l/2)):
#     if(a[i]==a[l-i-1]):
#         # print(i+" ",(l-i))
#         check=True
#     else:
#         check=False
#         break
# if(check):
#     print(1)
# else:
#     print(0)
import math
a=int(input())
slide=(math.sqrt(a/2**2+a**2))
print(slide*2+a)