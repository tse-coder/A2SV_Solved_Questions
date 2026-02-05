class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charDict = {}
        for char in chars:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
        res = 0
        for word in words:
            n = len(word)
            for letter in word:
                l = word.count(letter)
                if letter not in charDict or l > charDict[letter]:
                    break
            else:
                res += n
        return res
            