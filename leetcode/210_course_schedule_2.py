from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash, queue, ans = {}, [], []
        for i in range(numCourses):
            hash[i] = []
        for course in prerequisites:
            hash[course[0]].append(course[1])
            
        for course in list(hash):
            if len(hash[course]) == 0:
                queue.append(course)
                del hash[course]
                
        while len(queue) > 0:
            course = queue.pop(0)
            ans.append(course)
            
            for k in list(hash):
                if course in hash[k]:
                    hash[k].remove(course)

                if len(hash[k]) == 0:
                    queue.append(k)
                    del hash[k]
        
        return ans if len(ans) == numCourses else []
        

sol = Solution()
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# print(sol.findOrder(1, []))
# print(sol.findOrder(3, [[1,0],[1,2],[0,1]]))