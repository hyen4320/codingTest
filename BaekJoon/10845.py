'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
li=[]
def push(n):
    li.append(n)

def pop():
    if(len(li)==0):
        print(-1)
    else:
        print(li[0])
        li.remove(li[0])

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
    x=input().rstrip()
    if(x.startswith("push")):
        i,j=x.split(" ")
        push(j)
    elif(x.startswith("f")):
        front()
    elif(x.startswith("b")):
        back()
    elif(x.startswith('s')):
        size()
    elif(x.startswith('e')):
        empty()
    else:
        pop()

    