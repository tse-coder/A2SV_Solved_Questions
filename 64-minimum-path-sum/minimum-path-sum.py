class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if 0 <= i-1 < m and 0 <= j -1 <n:
                    grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
                elif 0 <= i-1 <m:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif 0 <= j - 1 < n:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
        return grid[-1][-1]
                