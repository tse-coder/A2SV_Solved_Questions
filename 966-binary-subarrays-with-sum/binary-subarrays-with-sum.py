class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_map = {0:1}
        running = 0
        res = 0
        for num in nums:
            running += num
            if running - goal in sum_map:
                res += sum_map[running-goal]
            sum_map[running] = sum_map.get(running,0) + 1
        return res