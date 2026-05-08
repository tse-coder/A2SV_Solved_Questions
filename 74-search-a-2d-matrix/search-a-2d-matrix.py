class Solution:
    def find(self,arr,target):
        idx = bisect.bisect_left(arr,target)
        return arr[idx] == target
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        l,r = 0,len(matrix)-1
        while l <= r:
            m = (l+r)//2
            cur = matrix[m]
            if cur[0] <= target <= cur[-1]:
                found = self.find(cur,target)
                break
            elif target < cur[0]:
                r = m - 1
            else:
                l = m + 1
        return found

