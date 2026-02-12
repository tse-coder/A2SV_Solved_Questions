class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numset1 = set(nums1)
        numset2 = set(nums2)
        res = []
        for num in numset2:
            if num in numset1:
                res.append(num)
        return res