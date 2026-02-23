class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height)-1
        l = 0
        max_area = min(height[l],height[r]) * (r-l)
        while r > l:
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area,(min(height[l],height[r]) * (r-l)))
        return max_area