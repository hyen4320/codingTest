class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0#앞부분
        self.rear = 0#뒷부분

    def isEmpty(self):
        return self.front ==self.rear# front와 rear가 같으면 공백상태
    
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity# front가 rear의 다음위치면 포화상태
    
    def enqueue(self, item):
        if not self.isFull():#포화가 아니면 삽입 가능.
            self.rear = (self.rear +1)% self.capacity#rear를 시계방행으로 회전
            self.array[self.rear]=item#그 위치에 새로운 요소를 저장
        else:pass

    def dequeue(self):
        if not self.isFull():# 포화가 아니면 삽입 가능
            self.front=(self.front+1)%self.capacity# front를 최전시키고
            return self.array[self.front]# 그 위치의 요소를 반환
        else:pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)% self.capacity]
        else: pass
    
    def size(self):
        return ( self.rear - self.front+self.capacity)%self.capacity
    