class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(img[0]) for _ in range(len(img))]
        r = len(img)
        c = len(img[0])
        for row in range(r):
            for col in range(c):
                total , count = 0,0
                for i in range(row-1,row+2):
                    for j in range(col-1,col+2):
                        if i >= r or i < 0 or j >= c or j < 0:
                            continue
                        total += img[i][j]
                        count += 1
                res[row][col] = total//count
        return res