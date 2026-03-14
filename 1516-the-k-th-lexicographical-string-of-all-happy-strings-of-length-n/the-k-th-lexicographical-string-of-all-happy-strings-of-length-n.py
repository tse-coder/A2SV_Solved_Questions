class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2**(n-1))
        if k > total:
            return ""
        res = []
        last= ""
        k -= 1
        
        for pos in range(n):
            branch = 2 ** (n-pos-1)
            chars = [c for c in "abc" if c!=last]
            idx = k//branch
            res.append(chars[idx])
            last = chars[idx]
            k %= branch
        
        return "".join(res)