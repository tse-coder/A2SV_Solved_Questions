class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        res.append(self.first(nums,target))
        res.append(self.last(nums,target))

        return res
    def first(self,arr,target):
        l,r = 0,len(arr)-1
        ans = -1
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == target:
                ans = m
                r = m - 1
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return ans
    
    def last(self, arr, target):
        l,r = 0,len(arr)-1
        ans = -1
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == target:
                ans = m
                l = m + 1
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return ans 