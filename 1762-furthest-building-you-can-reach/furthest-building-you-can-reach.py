class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        prevh = [0]*n

        for i in range(1,n):
            diff = heights[i]-heights[i-1]
            prevh[i] = diff if diff > 0 else 0

        heap = []
        k = i = 0
        while i < n:
            if prevh[i] > 0:
                heapq.heappush(heap,prevh[i])
            
            if ladders < len(heap):
                bricks -= heapq.heappop(heap)
            
            if bricks < 0:
                return i - 1
            i += 1
        return n - 1
