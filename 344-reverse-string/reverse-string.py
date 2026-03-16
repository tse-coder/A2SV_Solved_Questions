class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.left = 0
        self.right = len(s)-1
        def reverse(_s):
            if self.left >= self.right:
                return
            _s[self.left],_s[self.right] = _s[self.right],_s[self.left]
            self.left += 1
            self.right -= 1
            reverse(_s)
        reverse(s)