class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        s = sorted(nums)
        for i in range(len(nums)):
            res.append(bisect_left(s,nums[i]))
        return res