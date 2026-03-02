class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.arrPref = [0]
        for i in range(len(self.arr)):
            self.arrPref.append(self.arrPref[i]+self.arr[i])
    def sumRange(self, left: int, right: int) -> int:
        return self.arrPref[right+1] - self.arrPref[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)