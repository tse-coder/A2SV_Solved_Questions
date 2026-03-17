class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        for row in matrix:
            row.sort(reverse=True)
            idx = len(row)
            for i in range(idx):
                if row[i] == 0:
                    break
                max_area = max(max_area,row[i]*(i+1))

        return max_area
                