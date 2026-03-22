class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        d = maxDoubles
        count = 0
        while target > 1:
            if maxDoubles and target%2==0:
                target = target//2
                maxDoubles -= 1
            elif not maxDoubles:
                count += target-1
                break
            else:
                target -= 1
            count += 1
        return count