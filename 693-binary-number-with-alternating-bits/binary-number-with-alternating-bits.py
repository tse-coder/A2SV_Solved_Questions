class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nbin = bin(n)
        for i in range(len(nbin)-1):
            if nbin[i] == nbin[i+1]:
                return False
        return True