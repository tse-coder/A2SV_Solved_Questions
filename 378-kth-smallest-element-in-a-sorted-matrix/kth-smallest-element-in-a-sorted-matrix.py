import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        dup = []
        for row in matrix:
            dup.extend(row)
        
        heapq.heapify(dup)
        k -= 1
        while dup and k > 0:
            heapq.heappop(dup)
            k -= 1

        return dup[0]