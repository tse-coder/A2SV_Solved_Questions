class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for string in strs:
                if i >= len(string):
                    return common
                if string[i]!= curr:
                    return common
            else:
                common += curr
        return common