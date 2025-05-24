a,b=map(int,input().split(" "))
count=0

while a>=b:#a가 b이상이면 계속 나누기
    while a%b!=0:#N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        a-=1#뺼 때마다 
        count+=1#1더하기
    a//=b#b로 나누기
    count+=1#더하기
#마지막으로 나누 수에서 1씩 빼기
while a>1:
    a-=1
    count+=1

print(count)