class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deq = deque([])
        

    def insertFront(self, value: int) -> bool:
        if len(self.deq) < self.k:
           self.deq.append(value)
           return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.deq) < self.k:
            self.deq.appendleft(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.deq) > 0:
            self.deq.pop()
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if len(self.deq) > 0:
            self.deq.popleft()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if len(self.deq) > 0:
            return self.deq[-1]
        else:
            return -1
        

    def getRear(self) -> int:
        if len(self.deq) > 0:
            return self.deq[0]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.deq) >0:
            return False
        else:
            return True
        

    def isFull(self) -> bool:
        if len(self.deq) == self.k:
            return True
        else:
            return False
        