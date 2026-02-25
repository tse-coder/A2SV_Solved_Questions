class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        final = dict()
        br = 0
        for i in range(len(s)):
            final[s[i]] = i
        res = []
        for i in range(len(s)):
            br = max(br,final[s[i]])
            if i == br:
                if len(res) == 0:
                    res.append(i+1)
                else:
                    res.append((i+1)-sum(res))
        return res