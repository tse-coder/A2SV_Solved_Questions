class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        return (pow(4,n//2,MOD) * pow(5,(n//2) + (n%2),MOD)) % MOD