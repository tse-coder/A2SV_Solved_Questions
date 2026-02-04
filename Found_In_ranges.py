class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            found = False
            for rang in ranges:
                if rang[0]<= i and rang[1]>=i:
                    found = True
            if not found:
                return False
        return True
