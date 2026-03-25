class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        horizontal = [grid[i][j] for i in range(n) for j in range(m)]

        size = len(horizontal)
        for i in range(1,size):
            horizontal[i] += horizontal[i-1]

        canHorizontal = False
        for i in range(m-1,size,m):
            if horizontal[-1]-horizontal[i] == horizontal[i]:
                canHorizontal = True
                break
        
        vertical = [grid[i][j] for j in range(m) for i in range(n)]

        for i in range(1,size):
            vertical[i] += vertical[i-1]

        canVertical = False
        for i in range(n-1,size,n):
            if vertical[-1] - vertical[i] == vertical[i]:
                canVertical = True
                break
            
        return canVertical or canHorizontal