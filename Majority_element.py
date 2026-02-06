class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsMap = {}
        for num in nums:
            if num in numsMap:
                numsMap[num] += 1
            else:
                numsMap[num] = 1
        l = len(nums)//3 +1
        res = []
        for val in numsMap:
            if numsMap[val] >= l:
                res.append(val)
        return res