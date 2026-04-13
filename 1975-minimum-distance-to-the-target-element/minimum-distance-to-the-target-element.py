class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        _min = float("inf")
        for i , num in enumerate(nums):
            if num == target:
                _min = min(_min,abs(i-start))
        return _min