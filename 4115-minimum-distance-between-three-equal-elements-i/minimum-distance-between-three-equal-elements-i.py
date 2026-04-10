class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        min_dist = float("inf")
        for i , num in enumerate(nums):
            idx[num].append(i)

        for val in idx:
            if len(idx[val]) >= 3:
                for i in range(2,len(idx[val])):
                    dist = (
                        abs(idx[val][i-2] - idx[val][i-1])+
                        abs(idx[val][i-1] - idx[val][i])+
                        abs(idx[val][i-2] - idx[val][i]))
                    min_dist = min(dist,min_dist)
        return min_dist if min_dist != float("inf") else -1