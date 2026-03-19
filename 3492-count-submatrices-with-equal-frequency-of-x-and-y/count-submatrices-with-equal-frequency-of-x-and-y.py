class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        prefsum = [[[0,0] for _ in range(n+1)] for _ in range(m+1)]
        res = 0
        for r in range(m):
            for c in range(n):
                prefsum[r+1][c+1][0] = (
                    prefsum[r][c+1][0]+
                    prefsum[r+1][c][0]-
                    prefsum[r][c][0]+
                    int(grid[r][c] == "X")
                )
                prefsum[r+1][c+1][1] = (
                    prefsum[r][c+1][1]+
                    prefsum[r+1][c][1]-
                    prefsum[r][c][1]+
                    int(grid[r][c]=="Y")
                )
                if (
                    prefsum[r+1][c+1][0] >= 1 and 
                    prefsum[r+1][c+1][0] == prefsum[r+1][c+1][1]
                ):
                    res += 1
        return res
                    