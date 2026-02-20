class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_cnt = Counter(nums)
        res = []
        n = len(nums)
        for val in nums_cnt:
            if nums_cnt[val] > n//3:
                res.append(val)
        return res