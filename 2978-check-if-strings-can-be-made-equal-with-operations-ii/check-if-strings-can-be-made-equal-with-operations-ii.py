class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s2_odd_c = Counter([s2[i] for i in range(len(s2)) if i % 2 == 0])
        s2_even_c = Counter([s2[i] for i in range(len(s2)) if i % 2 == 1])
        s1_odd_c = Counter([s1[i] for i in range(len(s1)) if i % 2 == 0])
        s1_even_c = Counter([s1[i] for i in range(len(s1)) if i % 2 == 1])

        if s2_odd_c == s1_odd_c and s1_even_c == s2_even_c:
            return True
        return False
    