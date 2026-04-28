class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        print(points)
        arrow = 1
        cover = points[0][1]
        for i in range(1, len(points)):
            if points[i][0]>cover:
                arrow+=1
                cover = points[i][1]
            else:
                cover = min(cover, points[i][1])
        return arrow