class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(idx,path):
            res.add(tuple(path))
            if idx == len(nums):
                return
            
            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return list(res)
