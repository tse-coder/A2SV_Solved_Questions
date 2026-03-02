class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifter = [0]*len(s)
        for l,r,x in shifts:
            shifter[l] += 1 if x==1 else -1
            if r+1<len(s):
                shifter[r+1] -= 1 if x==1 else -1
        res = ''
        shift = 0
        for i,val in enumerate(shifter):
            shift += val
            res += chr( (ord(s[i]) - ord('a') + shift ) % 26 + ord("a"))
        return res