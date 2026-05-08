class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        nums = list(map(str,nums))
        reverse_map = dict()
        ans = float("inf")
        for i,num in enumerate(nums):
            if num in reverse_map:
                ans = min(ans,i - reverse_map[num])
            reverse_map[num.rstrip("0")[::-1]] = i
        return -1 if ans==float("inf") else ans
