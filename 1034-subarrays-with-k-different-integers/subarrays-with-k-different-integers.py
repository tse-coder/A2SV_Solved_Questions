class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayCounter(arr,p):
            l = 0
            count = 0
            ca = defaultdict(int)
            for r in range(len(arr)):
                ca[arr[r]] += 1
                while len(ca) > p:
                    ca[arr[l]] -= 1
                    if ca[arr[l]] == 0:
                        del ca[arr[l]]
                    l += 1
                count += r - l + 1
            return count
        return subarrayCounter(nums,k) - subarrayCounter(nums,k-1)