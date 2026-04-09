class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        _sorted = []
        res = []
        n = len(nums)
        for num in nums[::-1]:
            idx = bisect_left(_sorted,num)
            res.append(idx)
            insort(_sorted,num)
        return res[::-1]
