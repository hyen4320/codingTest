from itertools import combinations
def lcm(a,b):
    return (a*b)/gcd(a,b)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
