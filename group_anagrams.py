class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        for sr in strs:
            curr = "".join(sorted(list(sr)))
            if curr in strDict:
                strDict[curr].append(sr)
            else:
                strDict[curr] = [sr]
        res = []
        for val in strDict:
            res.append(strDict[val])
        return res