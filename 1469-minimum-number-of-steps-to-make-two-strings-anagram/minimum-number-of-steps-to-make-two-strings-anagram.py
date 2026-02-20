class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ct = Counter(t)
        res = 0
        for c in cs:
            if c not in ct:
                res += cs[c]
            elif cs[c] > ct[c]:
                res += cs[c] - ct[c]
        return res