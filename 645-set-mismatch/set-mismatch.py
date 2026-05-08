class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        dup = sum(nums) - sum(s)
        rem = sum(range(1,len(nums)+1)) - sum(s)
        return [dup,rem]