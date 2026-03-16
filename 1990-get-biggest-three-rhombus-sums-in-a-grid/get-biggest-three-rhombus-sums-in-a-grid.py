class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])

        sums = set()
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])

        for r in range(m):
            for c in range(n):
                k = 1
                while True:
                    if r + 2*k >= m or c - k < 0 or c + k >=n:
                        break
                    curr = 0
                    # top to right
                    for x in range(k):
                        curr += grid[r+x][c+x]

                    # right to bottom
                    for x in range(k):
                        curr += grid[r+k+x][c+k-x]

                    # bottom to left
                    for x in range(k):
                        curr += grid[r+2*k-x][c-x]

                    # left to top
                    for x in range(k):
                        curr += grid[r+k-x][c-k+x]
                    
                    sums.add(curr)
                    k+=1
        return sorted(list(sums),reverse=True)[:3]