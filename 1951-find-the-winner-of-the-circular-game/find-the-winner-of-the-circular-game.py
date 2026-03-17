class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(arr):
            if len(arr) == 1:
                return arr[0]
            else:
                idx = (k-1)%len(arr) 
                return helper(arr[idx+1:]+arr[:idx])
        return helper([i+1 for i in range(n)])