class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = s.split("0")
        count = 0
        for val in s:
            if len(val) > 0:
                count += 1
            if count > 1:
                return False
        return count == 1