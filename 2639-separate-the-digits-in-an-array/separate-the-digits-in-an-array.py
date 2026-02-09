class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        def separate(num):
            for val in str(num):
                res.append(int(val))
            
        for num in nums:
            separate(num)
        return res