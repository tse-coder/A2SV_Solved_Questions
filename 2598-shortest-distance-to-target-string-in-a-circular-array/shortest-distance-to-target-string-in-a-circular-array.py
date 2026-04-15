class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = float("inf")
        for i in range(n):
            if words[i] == target:
                dist = (startIndex - i)%n
                res = min(res,dist,abs(n-dist))
        return -1 if res == float("inf") else res