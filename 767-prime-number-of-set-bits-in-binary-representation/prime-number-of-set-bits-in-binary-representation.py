class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count  =  0
        for i in range(left,right+1):
            s = bin(i)
            s = list(s[2:])
            ones = s.count("1")
            if ones in {2,3,5,7,11,13,17,19}:
                count += 1
        return count