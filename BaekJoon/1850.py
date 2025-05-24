a,b=map(int,input().split(" "))


def gcd(_a,_b):
    while _b!=0:
        _a,_b=_b,_a%_b
    return _a

if(a-b<0):
    print('1'*gcd(b,a))
else:
    print('1'*gcd(a,b))
        
