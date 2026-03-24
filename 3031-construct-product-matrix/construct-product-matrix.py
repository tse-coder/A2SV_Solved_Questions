class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n,m = len(grid),len(grid[0])
        grid = [grid[i][j] for i in range(n) for j in range(m)]
        size = len(grid)
        pre = [1]*size
        suf = [1]*size
        for i in range(1,size):
            pre[i] = (pre[i-1]*grid[i-1])%MOD
        for i in range(size-2,-1,-1):
            suf[i] = (suf[i+1]*grid[i+1])%MOD
        res = [(pre[i]*suf[i])%MOD for i in range(size)]
        idx = 0
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = res[idx]
                idx += 1
        return ans

        