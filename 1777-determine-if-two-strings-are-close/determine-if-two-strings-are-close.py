class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        s1 = sorted([c1[val] for val in c1])
        s2 = sorted([c2[val] for val in c2])

        return s1 == s2 and set(word1) == set(word2)

