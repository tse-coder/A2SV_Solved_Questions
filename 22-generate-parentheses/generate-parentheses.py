class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o,c,path):
            if c > o:
                return
            if len(path)==2*n:
                if o == c:
                    res.append("".join(path))
                return
            for char in ("(",")"):
                path.append(char)
                backtrack(
                    o+1 if char=="(" else o,
                    c+1 if char==")" else c,
                    path
                )
                path.pop()
        backtrack(0,0,[])
        return res