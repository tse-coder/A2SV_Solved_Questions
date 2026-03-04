class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal = float("inf")
        startValue = 0
        for num in nums:
            startValue += num
            minVal = min(minVal,startValue)
        return (1 - minVal) if minVal < 0 else 1