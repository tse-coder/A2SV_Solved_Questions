class Solution:
    def addBinary(self, a: str, b: str) -> str:
        deca = int(a,2)
        decb = int(b,2)
        tot = deca + decb
        return bin(tot)[2:]