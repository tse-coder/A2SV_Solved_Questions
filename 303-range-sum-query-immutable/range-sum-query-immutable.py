class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        arrPref = [0]
        for i in range(len(self.arr)):
            arrPref.append(arrPref[i]+self.arr[i])
        return arrPref[right+1] - arrPref[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)