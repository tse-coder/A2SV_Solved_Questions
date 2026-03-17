class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num,exp):
            if exp == 0:
                return 1
            half = helper(num,exp//2)
            if exp % 2:
                return num * half * half
            else:
                return half * half
            
        
        if n < 0:
            x = 1/x
            n = -n
        
        return helper(x,n)