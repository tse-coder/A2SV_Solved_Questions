class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        max_num = nums[0]
        print("nums_counter:",nums_counter)
        for val in nums_counter:
            if nums_counter[val] > nums_counter[max_num]:
                max_num = val
        f1 = 0
        f2 = nums_counter[max_num]
        for i in range(0,len(nums)):
            if nums[i] == max_num:
                f1 += 1
                f2 -= 1
            if f1 > (i+1)//2 and f2 > (len(nums)-i-1)//2:
                return i
        
        return -1