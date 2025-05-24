N=int(input())
stack=[0]*N

for i in range(N):
    num=int(input())
    stack.pop() if num == 0 else stack.append(num)
print(sum(stack))