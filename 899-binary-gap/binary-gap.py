class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        l,r = 0,0
        res = 0

        for r in range(len(s)):
            if s[r] == "1":
                res = max(res,r-l)
                l = r
        return res