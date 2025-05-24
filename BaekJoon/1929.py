##에라토스테네스의 채
import math
def prime_list(n,m):
    sieve=[True]*(m-n+1)
    # print(sieve)
    for x in range(n,int(math.sqrt(m)+1)):
        if(x%2==0):
            for y in range(0,m,x):
                sieve[y-n]=False
    print(sieve)
    return [_ for _ in range(n,m) if sieve[_-n]]
a,b=map(int,input().split(" "))
print(prime_list(a,b))
