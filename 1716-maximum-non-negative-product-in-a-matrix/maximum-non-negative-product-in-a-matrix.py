class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m , n = len(grid),len(grid[0])
        minmaxprod = [[[0,0] for _ in range(n)] for _ in range(m)]
        minmaxprod[0][0] = [grid[0][0],grid[0][0]]
        for i in range(1,m):
            minmaxprod[i][0] = [grid[i][0] * minmaxprod[i-1][0][0],grid[i][0] * minmaxprod[i-1][0][0]]
        for i in range(1,n):
            minmaxprod[0][i] = [grid[0][i] * minmaxprod[0][i-1][0],grid[0][i] * minmaxprod[0][i-1][0]]
        
        for r in range(1,m):
            for c in range(1,n):
                candidates = [
                    grid[r][c] * minmaxprod[r-1][c][0],
                    grid[r][c] * minmaxprod[r-1][c][1],
                    grid[r][c] * minmaxprod[r][c-1][0],
                    grid[r][c] * minmaxprod[r][c-1][1]
                ]
                minmaxprod[r][c] = [min(candidates),max(candidates)]
                
        maxProd = minmaxprod[m-1][n-1][1]
        return (maxProd)%(10**9 + 7) if maxProd >= 0 else -1