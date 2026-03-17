class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = dict()

        @lru_cache
        def f(n, s):
            # 1 7 7
            if n == 1:
                return 5 if s == 0 else 4
            
            ans = 1
            if n % 2 == 1:
                n -= 1
                # 1 2 2
                return ((5 if not s else 4) * f(n // 2, s ^ 1) * f(n // 2, s ^ (((n // 2) & 1) == 0))) % MOD
            else:
                y = f(n // 2, s)
                x = f(n // 2, s ^ ((n // 2) & 1))
                return (x * y) % MOD

        return f(n, 0)