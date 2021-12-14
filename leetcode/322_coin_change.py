from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for i in range(amount+1)] 
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                # print(i)
                if coins[j] <= i:
                    amt_left = i - coins[j]
                    steps = 1 + dp[amt_left]
                    dp[i] = min(dp[i], steps)
        
        return dp[amount] if dp[amount] != math.inf else -1

sol = Solution()
output = sol.coinChange([1], 2)
print(output)