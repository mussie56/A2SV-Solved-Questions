class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0]*k
        self.head = 0
        self.rear = -1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size < len(self.deque):
            self.head-=1
            if self.head == -1:
                self.head = len(self.deque)-1
            self.deque[self.head] = value
            self.size+=1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < len(self.deque):
            self.rear+=1
            if self.rear == len(self.deque):
                self.rear = 0
            self.deque[self.rear] = value
            self.size+=1
            return True
        return False  

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.head+=1
            if self.head == len(self.deque):
                self.head = 0
            self.size-=1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.rear-=1
            if self.rear == -1:
                self.rear = len(self.deque)-1
            self.size-=1
            return True
        return False

    def getFront(self) -> int:
        if self.size > 0:
            return self.deque[self.head]
        return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.deque[self.rear]        
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.deque)