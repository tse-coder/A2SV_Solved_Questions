class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1,len(nums)
        while l < r:
            m = (l+r)//2
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= m:
                    cnt += 1
            if cnt > m:
                r = m
            else:
                l = m + 1

        return l
                