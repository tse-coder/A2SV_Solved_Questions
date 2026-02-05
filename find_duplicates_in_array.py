class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                res.append(nums[i])
            visited.add(nums[i])
        return res
                