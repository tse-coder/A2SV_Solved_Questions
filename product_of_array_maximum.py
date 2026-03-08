class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefs = [num for num in nums]
        posts = [num for num in nums]

        for i in range(1,len(nums)):
            prefs[i] = nums[i] * prefs[i-1]

        for i in range(len(nums)-2,-1,-1):
            posts[i] = nums[i] * posts[i+1]

        res = [posts[1]]

        for i in range(1,len(nums)-1):
            res.append(posts[i+1]*prefs[i-1])

        res.append(prefs[-2])

        return res