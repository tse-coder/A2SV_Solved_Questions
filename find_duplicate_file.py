class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = []
        dupDict = {}
        for path in paths:
            spl = path.split()
            root = spl[0]
            temp = []
            for p in spl[1:]:
                s = p.split("(")
                if s[1] not in dupDict:
                    dupDict[s[1]] = [root+ "/" + s[0]]
                else:
                    dupDict[s[1]].append(root  + "/" + s[0])
        for val in dupDict:
            if len(dupDict[val]) != 1:
                res.append(dupDict[val])
        return res


