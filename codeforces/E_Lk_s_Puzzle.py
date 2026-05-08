n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

visited = [[False]*m for _ in range(n)]
dxns = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(y,x,py,px):
    if visited[y][x]:
        return True
    visited[y][x] = True
    
    for dy,dx in dxns:
        ny,nx = y+dy,x+dx
        if (
            0<=nx<m and
            0<=ny<n and 
            grid[y][x] == grid[ny][nx] and
            (py!=y and px!=x) and
            dfs(ny,nx,y,x)):
            return True
    else:
        return False
    
for i in range(n):
    for j in range(m):
        if dfs(i,j,-1,-1):
            print("Yes")
            exit()

print("No")
