class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in t:
            if char in s and s.count(char)==t.count(char):
                continue
            else:
                return False

        return False if len(t) != len(s) else True