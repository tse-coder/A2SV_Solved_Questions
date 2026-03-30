class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = list(s)
        res = set()
        min_diff = len(s)
        def removePar(i,o,c,path):
            nonlocal min_diff, res
            if i == len(s):
                if o != c or "".join(path) in res:
                    return
                len_diff = len(s) - len(path)
                if len_diff < min_diff:
                    res = set(["".join(path)])
                    min_diff = len_diff
                elif len_diff == min_diff:
                    res.add("".join(path))
                return
            if c > o:
                return
            if s[i] == "(":
                removePar(i+1,o,c,path)
                removePar(i+1,o+1,c,path+["("])
            elif s[i] == ")":
                removePar(i+1,o,c,path)
                removePar(i+1,o,c+1,path+[")"])
            else:
                removePar(i+1,o,c,path+[s[i]])
        removePar(0,0,0,[])
        return list(res)