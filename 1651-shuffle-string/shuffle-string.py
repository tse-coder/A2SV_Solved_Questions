class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        two = []
        for i in range(len(s)):
            two.append([indices[i],s[i]])
        two.sort()
        res = ""
        for val in two:
            res+=val[1]
        return res