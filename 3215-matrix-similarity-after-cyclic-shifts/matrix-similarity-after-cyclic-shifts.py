class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        cp = [row[:] for row in mat]
        def leftShift(arr):
            temp = arr[0]
            for i in range(1,len(arr)):
                arr[i-1] = arr[i]
            arr[-1] = temp
        
        def rightShift(arr):
            temp = arr[-1]
            for i in range(len(arr)-1,0,-1):
                arr[i] = arr[i-1]
            arr[0] = temp
        
        par = True

        for i in range(k):
            for row in mat:
                if par:
                    leftShift(row)
                else:
                    rightShift(row)
                par = not par
            par=True

        return mat == cp
