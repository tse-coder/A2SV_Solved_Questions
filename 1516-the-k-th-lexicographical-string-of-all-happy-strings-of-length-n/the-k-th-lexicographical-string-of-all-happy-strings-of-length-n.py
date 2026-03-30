class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        choices = ["a","b","c"]
        def backtrack(path):
            if len(path) == n:
                res.append("".join(path))
                return
            for ch in choices:
                if path and path[-1] == ch:
                    continue
                path.append(ch)
                backtrack(path)
                path.pop()
        backtrack([])
        
        return "" if k > len(res) else res[k-1]
            
        