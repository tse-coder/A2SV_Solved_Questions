class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        total_sum = 0
        for i in range(n):
            for j in range(m):
                total_sum += grid[i][j]
        if total_sum & 1:
            return False
        total_sum = total_sum//2
        _sum = 0
        for i in range(n):
            if _sum == total_sum:
                return True
            if _sum > total_sum:
                break
            _sum += sum(grid[i])
        _sum = 0
        for j in range(m):
            if _sum == total_sum:
                return True
            if _sum > total_sum:
                break
            for i in range(n):
                _sum += grid[i][j]
        return False