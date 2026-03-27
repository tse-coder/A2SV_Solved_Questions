from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.deff = 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.deff = 0
            return False
        else:
            self.deff += 1

        if self.deff >= self.k:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)