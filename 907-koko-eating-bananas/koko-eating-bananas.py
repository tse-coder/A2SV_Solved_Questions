import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k):
            tot = 0
            for p in piles:
                tot += math.ceil(p/k)

            return tot <= h
        
        left,right = 1, max(piles)
        ans = right
        while left <= right:
            mid = left + (right-left)//2
            if canfinish(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans