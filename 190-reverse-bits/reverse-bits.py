class Solution:
    def reverseBits(self, n: int) -> int:
        nbin = bin(n)[2:].zfill(32)
        nreversed = nbin[::-1]
        return int(nreversed,2)