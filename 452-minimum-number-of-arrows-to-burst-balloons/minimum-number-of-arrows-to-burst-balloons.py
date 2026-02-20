class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        line = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > line:
                count += 1
                line = points[i][1]
            else:
                line = min(points[i][1],line) 
        return count
