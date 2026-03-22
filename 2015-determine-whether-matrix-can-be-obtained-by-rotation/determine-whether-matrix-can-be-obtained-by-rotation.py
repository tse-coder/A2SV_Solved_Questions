class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # rotate clockwise
        def rotateNinty(matrix):
            for i in range(len(matrix)):
                for j in range(i+1,len(matrix[0])):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            for i in range(len(matrix)):
                matrix[i] = matrix[i][::-1]
            

        for i in range(4):
            rotateNinty(mat)
            if mat == target:
                return True
        return False

