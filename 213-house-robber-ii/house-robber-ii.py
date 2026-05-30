class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            for i in range(2,len(arr)):
                arr[i] = arr[i] + max(arr[:i-1])
            return max(arr)
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
