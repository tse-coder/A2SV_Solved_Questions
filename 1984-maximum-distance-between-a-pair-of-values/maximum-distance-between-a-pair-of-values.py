class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        res = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                j += 1
            if j-1 >= i:
                res = max(res,j - 1 - i)
        return res