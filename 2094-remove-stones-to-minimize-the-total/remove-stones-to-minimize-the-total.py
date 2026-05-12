class SpecialNumber:
    def __init__(self,val):
        self.val = val
    def __lt__(self,other):
        return self.val > other.val
    def __repr__(self):
        return repr(self.val)

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        tot = sum(piles)
        for pile in piles:
            heapq.heappush(heap,SpecialNumber(pile))
        for _ in range(k):
            _val = heapq.heappop(heap).val
            remove = _val//2
            _new = _val - remove
            tot -= remove
            heapq.heappush(heap,SpecialNumber(_new))

        return tot
        
