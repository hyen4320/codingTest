def lcm(a,b):
    return (a*b)/gcd(a,b)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a,b=map(int,input().split(" "))
if(a-b<0):
    # print(gcd(b,a))
    print(int(lcm(b,a)))
else:
    # print(gcd(a,b))
    print(int(lcm(a,b)))

