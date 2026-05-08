class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for i in range(count[0]):
            nums[i]=0
        for i in range(count[1]):
            nums[i+count[0]] = 1
        for i in range(count[2]):
            nums[i+count[1]+count[0]] = 2

        