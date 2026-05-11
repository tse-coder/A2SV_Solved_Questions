import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        pq = []

        for x in nums1:
            heapq.heappush(pq,(x+nums2[0],0))

        while k > 0 and pq:
            x,idx = heapq.heappop(pq)
            res.append([x-nums2[idx],nums2[idx]])
            if idx + 1 < len(nums2):
                heapq.heappush(pq,(x-nums2[idx]+ nums2[idx+1], idx + 1))
            k -= 1
    
        return res