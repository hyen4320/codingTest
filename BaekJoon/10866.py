'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
li=[]
def push_front(n):
    li.reverse()
    li.append(n)
    li.reverse()
    
def push_back(n):
    li.append(n)
def pop_front():
    if(len(li)==0):
        print(-1)
    else:
        print(li.pop(0))
def pop_back():
    if(len(li)==0):
        print(-1)
    else:
        print(li.pop())

def size():
    print(len(li))
def empty():
    if(len(li)==0):
        print(1)
    else:
        print(0)
def front():
    if(len(li)==0):
        print(-1)
    else:
        print(li[0])
def back():
    if(len(li)==0):
        print(-1)
    else:
        print(li[-1])
input=sys.stdin.readline
N=int(input())

for i in range(N):
    x=input().rstrip("\n")
    if(x.startswith("push_front")):
        i,j=x.split(" ")
        push_front(int(j))
    elif(x.startswith("push_back")):
        i,j=x.split(" ")
        push_back(int(j))
    elif(x.startswith("f")):
        front()
    elif(x.startswith("b")):
        back()
    elif(x.startswith('s')):
        size()
    elif(x.startswith('e')):
        empty()
    elif(x.startswith('pop_front')):
        pop_front()
    else:
        pop_back()

    