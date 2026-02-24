class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        r = len(skill) - 1
        l = 0
        pairs = []
        while l < r:
            pairs.append((skill[l],skill[r]))
            r -= 1
            l += 1
        team = sum(pairs[0])
        res = 0
        for pair in pairs:
            if sum(pair) != team:
                return -1
            res += pair[0]*pair[1]
        return res
        