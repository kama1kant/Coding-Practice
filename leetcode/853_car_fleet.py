from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time, n, ans, p = [], len(position), 1, 0
        zipped = sorted(list(zip(position, speed)), key=lambda x:x[0], reverse=True)
        position, speed = zip(*zipped)

        for i in range(n):
            time.append((target-position[i])/speed[i])
        
        for i in range(1, n):
            if time[p] < time[i]:
                ans += 1
                p = i
            
        return ans
        
sol = Solution()
print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(sol.carFleet(10, [3], [3]))
print(sol.carFleet(10, [6,8], [3,2]))
print(sol.carFleet(10, [8,3,7,4,6,5], [4,4,4,4,4,4]))
print(sol.carFleet(10, [2,4], [3,2]))