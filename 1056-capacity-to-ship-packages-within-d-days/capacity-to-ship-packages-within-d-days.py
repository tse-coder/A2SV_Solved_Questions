class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            curr = 0
            count = 0
            for w in weights:
                if curr + w <= m:
                    curr += w
                else:
                    curr = w
                    count += 1
            if count+1 > days:
                l = m + 1
            else:
                r = m - 1

        return l