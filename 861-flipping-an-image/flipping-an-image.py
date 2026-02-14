class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            curr = []
            for j in range(len(image[i])-1,-1,-1):
                curr.append((image[i][j]+1)%2)
            image[i] = curr
        return image