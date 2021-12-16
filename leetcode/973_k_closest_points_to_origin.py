from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucledianDistance(point1, point2):
            return pow(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2), 1/2)
        
        distance_arr = []
        distance_map = {}
        for point in points:
            distance = eucledianDistance(point, [0, 0])
            distance_arr.append(distance)
            if str(distance) not in distance_map:
                distance_map[str(distance)] = []
            distance_map[str(distance)].append(point)
        
        distance_arr = [eucledianDistance(point, [0, 0]) for point in points]
        # print(distance_map, distance_arr)

        ans = []
        nearest = heapq.nsmallest(k, distance_arr)
        for point in nearest:
            ans += distance_map[str(point)]
                
        return ans[:k]
        

sol = Solution()
output = sol.kClosest([[0, 1], [1, 0]], 2)
print(output)