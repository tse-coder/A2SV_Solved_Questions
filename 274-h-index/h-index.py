class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        citations.sort()
        res = 0
        for h in range(1,n+1):
            idx = bisect_left(citations,h)
            if h <= n - idx:
                res = h
        return res