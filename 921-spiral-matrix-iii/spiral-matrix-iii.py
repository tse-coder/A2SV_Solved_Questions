class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        j = cStart
        i = rStart
        res.append([i,j])
        step = 1
        while len(res) < rows*cols:
            # go right
            for _ in range(step):
                j += 1
                if j < cols and j >= 0 and i < rows and i >= 0:
                    res.append([i,j])
            
            # go down
            for _ in range(step):
                i += 1
                if i >= 0 and i < rows and j < cols and j >= 0:
                    res.append([i,j])
            
            step += 1
            # go left 
            for _ in range(step):
                j -= 1
                if j < cols and j >= 0 and i < rows and i >= 0:
                    res.append([i,j])
            
            # go up
            for _ in range(step):
                i -= 1
                if j < cols and j >= 0 and i < rows and i >= 0:
                    res.append([i,j])

            step += 1
        return res