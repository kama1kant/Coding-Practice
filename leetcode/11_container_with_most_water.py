from typing import List
import math


class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, e = 0, len(height)-1
        area = -math.inf
        
        while s < e:
            area = max(area, min(height[s], height[e]) * (e-s))
            if height[s] < height[e]:
                s += 1
            else: 
                e -= 1
        return area
            
        
sol = Solution()
output = sol.maxArea([2, 3, 4, 5, 18, 17, 6])
print(output)
