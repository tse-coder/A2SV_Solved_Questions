class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        min_dist = float("inf")
        for i,num in enumerate(nums):
            idx[num].append(i)
        for val in idx:
            if len(idx[val]) >= 3:
                for i in range(2,len(idx[val])):
                    min_dist = min(min_dist,(
                        abs(idx[val][i] - idx[val][i-1]) +
                        abs(idx[val][i-1] - idx[val][i-2]) +
                        abs(idx[val][i] - idx[val][i-2])
                    ))
        return -1 if min_dist == float("inf") else min_dist