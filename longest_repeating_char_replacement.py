class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            max_freq = max(freqs.values())
            if r - l + 1 - max_freq > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res,r - l + 1)
        return res
