class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = list(s) # alternates that start with 0
        c1 = 0

        for i,val in enumerate(alt1):
            if i == 0 and val == "1":
                c1 += 1
                alt1[i] = "0"
            elif alt1[i-1] == alt1[i] and i > 0:
                c1 += 1
                alt1[i] = "1" if alt1[i-1] == "0" else "0"
        
        alt2 = list(s) # alternates start with 1
        c2 = 0
        for i,val in enumerate(alt2):
            if i == 0 and val == "0":
                c2 += 1
                alt2[i] = "1"
            elif alt2[i-1] == alt2[i] and i > 0:
                c2 += 1
                alt2[i] = "1" if alt2[i-1] == "0" else "0"
    
        return min(c1,c2)