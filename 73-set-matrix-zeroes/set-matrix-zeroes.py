class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_indices = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j not in zero_indices:
                        zero_indices[j] = ["x"]
                    else:
                        zero_indices[j].append("x")
                    if i not in zero_indices:
                        zero_indices[i] = ["y"]
                    else:
                        zero_indices[i].append("y")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in zero_indices and "y" in zero_indices[i]) or (j in zero_indices and "x" in zero_indices[j]):
                    matrix[i][j] = 0
                    
        return matrix        