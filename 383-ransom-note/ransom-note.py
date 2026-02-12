class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(list(ransomNote))
        magazineCounter = Counter(list(magazine))

        for char in ransomNote:
            if char not in magazineCounter or magazineCounter[char] < ransomCounter[char]:
                return False
        return True