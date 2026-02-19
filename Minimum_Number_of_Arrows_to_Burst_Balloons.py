class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse = True)
        p = points[0][0]
        count = 1
        for i in range(1,len(points)):
            if p <= points[i][1]:
                continue
                
            count+=1
            p = points[i][0]

        return count
