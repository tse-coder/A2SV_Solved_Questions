class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        prefmat =[[0]*(n+1) for _ in range(m+1)]
        count = 0
        for r in range(m):
            for c in range(n):
                prefmat[r+1][c+1] = grid[r][c] + prefmat[r+1][c] + prefmat[r][c+1] - prefmat[r][c]
                if prefmat[r+1][c+1] <= k:
                    count += 1
        return count
