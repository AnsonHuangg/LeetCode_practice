class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        count = []
        for i in range(len(queries)):
            count.append(0)
            for j in range(len(points)):
                if ( (points[j][0]-queries[i][0])**2+(points[j][1]-queries[i][1])**2-queries[i][2]**2 ) <= 0:
                    count[i] += 1
        return count
