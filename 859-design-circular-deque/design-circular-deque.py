class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k + 1
        self.q = [0]*self.size
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front + 1) % self.size
        self.q[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear - 1) % self.size
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front - 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.rear = (self.rear + 1) % self.size
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.q[self.front]
        return -1        

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.q[(self.rear + 1) % self.size]
        return -1

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.front + 1) % self.size == self.rear


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()