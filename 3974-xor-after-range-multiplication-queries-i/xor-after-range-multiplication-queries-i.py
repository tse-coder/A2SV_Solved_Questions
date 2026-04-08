class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l,r,k,v = query
            idx = l
            while idx <= r and idx < len(nums):
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k
        
        res = nums[0]
        for i in range(1,len(nums)):
            res ^= nums[i]
        return res