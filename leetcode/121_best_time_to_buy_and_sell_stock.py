from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = math.inf
        high = -math.inf
        max_profit = 0
        
        for price in prices:
            if price < low:
                low = price                
                high = -math.inf
            elif price > high:
                high = price
            
            max_profit = max(max_profit, high-low)
        
        return max_profit
            
        
sol = Solution()
output = sol.maxProfit([7, 1, 5, 3, 6, 4])
print(output)
