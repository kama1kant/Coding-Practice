class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dict, ans = {}, 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i], points[j]
                d = str(pow((pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)), 0.5))
                for e in [a, b]:
                    id = str(e[0])+'-'+str(e[1])
                    if id not in dict: dict[id] = {}
                    if d not in dict[id]: dict[id][d] = 0
                    dict[id][d] += 1
                    
        for point in dict:
            for d in dict[point]:
                if dict[point][d] > 1:
                    ans += dict[point][d] * (dict[point][d]-1)
        
        return ans
        
sol = Solution()
print(sol.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
print(sol.numberOfBoomerangs([[1,1],[2,2],[3,3]]))
print(sol.numberOfBoomerangs([[1,1]]))
print(sol.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))