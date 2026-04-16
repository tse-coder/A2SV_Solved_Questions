class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        l,r = 1, max(candies)
        while l < r:
            m = (l+r+1)//2
            if self.can_allocate(m,candies,k):
                l = m
            else:
                r = m - 1
        return l
    def can_allocate(self,m,candies,k):
        max_child = 0
        for pile in candies:
            max_child += pile // m
        return max_child >= k