class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m,n = len(grid),len(grid[0])
        dxns = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False]*n for _ in range(m)]

        def dfs(y,x):
            visited[y][x] = True
            for dy,dx in dxns:
                nx,ny = x+dx,y+dy
                if 0 <=nx<n and 0<=ny<m:
                    if not visited[ny][nx] and grid[ny][nx] == "1":
                        dfs(ny,nx)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=="1":
                    dfs(i,j)
                    islands += 1

        return islands