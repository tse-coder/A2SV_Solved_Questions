class Solution:
    def findMinDist(self,arr,n,q):
        if len(arr) == 1:
            return -1
        i = bisect.bisect_left(arr, q)
        prev_idx = arr[i-1] if i > 0 else arr[-1]
        next_idx = arr[i+1] if i < len(arr)-1 else arr[0]
        
        d1 = abs(q - prev_idx)
        d2 = abs(q - next_idx)
        return min(d1, n - d1,d2, n - d2)

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        same = defaultdict(list)
        for i,num in enumerate(nums):
            same[num].append(i)
        res = []
        for query in queries:
            val = nums[query]
            res.append(self.findMinDist(same[val],len(nums),query))
        return res