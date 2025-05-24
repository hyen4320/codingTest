class ArrayStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    # 스택의 연산들을 멤버 함수로 구현
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.top ==self.capacity-1
    def push(self,e):
        if not self.isFull():
            self.top+=1
            self.array[self.top]=e
        else:pass
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array[self.top+1]
        else:pass
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:pass
def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('{','[', '('):
            stack.push(ch)
        elif ch in('}',']',')'):
            if stack.isEmpty():
                return False
            else:
                left=stack.pop()
                if(ch =='}' and left !='{') or \
                (ch==']'and left !='[')or \
                (ch==')'and left !='('):
                    return False
    return stack.isEmpty()
N=int(input())
for i in range(N):
    s=input()
    if(checkBrackets(s)):
        print("YES")
    else:
        print('NO')