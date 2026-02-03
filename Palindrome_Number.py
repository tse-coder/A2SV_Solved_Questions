class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(len(s)//2):
            if s[i] != s[n-i-1]:
                return False
        return True
