class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1,arr2):
            l,r,ans = 0,0,[]
            while l < len(arr1) and r < len(arr2):
                if arr1[l] < arr2[r]:
                    ans.append(arr1[l]) 
                    l += 1
                else:
                    ans.append(arr2[r])
                    r += 1
            ans.extend(arr1[l:])
            ans.extend(arr2[r:])
            return ans

        if len(nums) == 1:
            return nums
        left_half = nums[:len(nums)//2]
        right_half = nums[len(nums)//2:]

        sorted_left = self.sortArray(left_half)
        sorted_right = self.sortArray(right_half)

        return merge(sorted_left,sorted_right)