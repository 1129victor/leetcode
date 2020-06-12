class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        
        for i in range(0, len(points) - 1):
            x_dis = abs(points[i][0] - points[i + 1][0])
            y_dis = abs(points[i][1] - points[i + 1][1])
            count += max(x_dis, y_dis)
        return count
