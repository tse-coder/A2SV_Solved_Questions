class Solution:
    def customSortString(self, order: str, s: str) -> str:
        level = dict()
        for i , c in enumerate(order):
            level[c] = i
        for c in s:
            if c not in order:
                level[c] = float("inf")
        s = list(s)
        s.sort(key=lambda x : level[x])

        return "".join(s)

