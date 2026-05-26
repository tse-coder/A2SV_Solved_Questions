class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_prf = 0
        mn_prs = float("inf")
        for p in prices:
            mn_prs = min(mn_prs,p)
            mx_prf = max(mx_prf,p-mn_prs)
        return mx_prf