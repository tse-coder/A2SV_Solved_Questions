class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        l,r = 0,len(colors)-1
        j = r
        while j > l and colors[j] == colors[l]:
            j -= 1
        i = l
        while i < r and colors[i] == colors[r]:
            i += 1
        return max(j-l,r-i)

