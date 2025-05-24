capacity = 10
array = [None]*capacity
top = -1
def isEmpty():# 공백상태
    if top==-1 : return True
    else :  return  False

def isFull():# 포화상태
    return top == capacity-1 # 탑의 상태를 반환

def push(e):
    global top # top은 전역변수
    if not isFull():
        top +=1
        array[top] = e
    else :
        print("stack overflow")
        exit()

def pop():
    global top
    if not isEmpty():
        top -=1# 탑 먼저 감소
        return array[top+1]
    else:
        print("stack underflow")
        exit()

def peek():# 상단요소 보기만 함
    if not isEmpty():
        return array[top]#공백이 아닐 때 top위치의 요소 반환
    else: pass
    
