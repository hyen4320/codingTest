N=int(input())
a=350.34
b=230.90
c=190.55
d=125.30
e=180.90
for i in range(N):
    f=list(map(float,input().split()))
    print("$%0.2f"%(f[0]*a+f[1]*b+f[2]*c+f[3]*d+f[4]*e))
