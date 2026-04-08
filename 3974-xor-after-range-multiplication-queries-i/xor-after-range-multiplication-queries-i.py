class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = (10**9 + 7)
        for l,r,k,v in queries:
            idx = l
            while idx <= r and idx < len(nums):
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        
        res = nums[0]
        for i in range(1,len(nums)):
            res ^= nums[i]
        return res