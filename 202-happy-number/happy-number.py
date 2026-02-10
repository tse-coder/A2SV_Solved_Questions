class Solution:
    def isHappy(self, n: int) -> bool:
        def split(num):
            nums = list(str(num))
            splitSum = 0
            for val in nums:
                splitSum += int(val)**2
            
            return splitSum

        visited = set()
        while True:
            n = split(n)
            print(n)
            if n == 1:
                return True
            if n not in visited:
                visited.add(n)
            else:
                return False
        return True
