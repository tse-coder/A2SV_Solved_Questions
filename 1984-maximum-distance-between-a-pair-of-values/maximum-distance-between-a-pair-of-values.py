class Solution:
    def find_index(self,nums,val):
        l,r = 0,len(nums)-1
        ans = -1
        while l <= r :
            m = (l+r)//2

            if nums[m] >= val:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
            
        


    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums1):
            idx = self.find_index(nums2,num)
            if idx >= i:
                res = max(res,idx-i)
        return res