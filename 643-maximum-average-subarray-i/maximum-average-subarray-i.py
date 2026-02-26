class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = curr = sum(nums[:k])
        for l in range(1,len(nums)-k+1):
            curr = curr + nums[l+k-1] - nums[l-1]
            res = max(curr,res)
        return res/(k)
            
