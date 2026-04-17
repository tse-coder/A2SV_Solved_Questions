class Solution:
    # def quickSort(self,arr,left,right):
    #     if left >= right:
    #         return
    #     pivot = self.partition(arr,left,right)
    #     self.quickSort(arr,left,pivot-1)
    #     self.quickSort(arr,pivot+1,right)
    # def partition(self,arr,left,right):
    #     j = left
    #     for i in range(left,right):
    #         if arr[i] < arr[right]:
    #             arr[i],arr[j] = arr[j],arr[i]
    #             j += 1
    #     arr[j],arr[right] = arr[right],arr[j]
    #     return j
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # self.quickSort(nums,0,len(nums)-1)
        nums.sort()
        ans = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                ans.append(nums[i])
        return ans