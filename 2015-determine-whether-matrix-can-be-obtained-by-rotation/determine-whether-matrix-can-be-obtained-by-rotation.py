class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateNinty(mat):
            for i in range(len(mat)):
                for j in range(i+1,len(mat)):
                    mat[i][j] ,mat[j][i] = mat[j][i],mat[i][j]
            for i in range(len(mat)):
                mat[i] = mat[i][::-1]
            return mat
        for i in range(4):
            if rotateNinty(mat) == target:
                return True
        return False