class Solution:
    def findValidPair(self, s: str) -> str:
        s_counter = Counter(s)
        for i in range(1,len(s)):
            if int(s[i]) == s_counter[s[i]] and int(s[i-1]) == s_counter[s[i-1]] and s[i]!=s[i-1]:
                return s[i-1:i+1]
        return ""
        