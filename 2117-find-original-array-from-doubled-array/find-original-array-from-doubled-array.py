class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []
        c = Counter(changed)
        s = set(changed)
        changed.sort()
        res = []
        for val in changed:
            if val in c and c[val] >= 1:
                c[val] -= 1
                if (val*2) in c and c[(val*2)] >= 1:
                    res.append(val)
                    c[val*2] -= 1
                    
            
            if len(res) == len(changed)//2:
                return res        
        return []
        
        