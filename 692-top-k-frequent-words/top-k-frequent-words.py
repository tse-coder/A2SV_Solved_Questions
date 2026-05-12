from collections import Counter
class ReverseStr:
    def __init__(self, val):
        self.val = val
    
    def __lt__(self, other):
        return self.val > other.val
    
    def __gt__(self,other):
        return self.val < other.val
    
    def __repr__(self):
        return repr(self.val)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        for word, count in c.items():
            heapq.heappush(heap,(count,ReverseStr(word)))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []

        while heap:
            cnt,ww = heapq.heappop(heap)
            res.append(ww.val)

        return res[::-1]
        