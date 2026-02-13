class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        pat_dict = {}
        taken = set()
        if len(strs) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in pat_dict:
                if pat_dict[pattern[i]] != strs[i]:
                    return False
            else:
                if strs[i] in taken:
                    return False
                pat_dict[pattern[i]] = strs[i]
                taken.add(strs[i])
        return True