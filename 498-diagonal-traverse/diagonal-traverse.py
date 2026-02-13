class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        parts = [[] for _ in range (len(mat)+len(mat[0])-1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                parts[i+j].append(mat[i][j])
        for i in range(len(parts)):
            if i % 2 == 0:
                for j in range(len(parts[i])-1,-1,-1):
                    res.append(parts[i][j])
            else:
                for j in range(len(parts[i])):
                    res.append(parts[i][j])
        return res
