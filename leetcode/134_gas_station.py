from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas, totalCost, curGas, start = 0, 0, 0, 0
        
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            curGas += gas[i] - cost[i]
            if curGas < 0:
                start = i + 1
                curGas = 0
            
        return start if totalGas - totalCost >= 0 else -1

sol = Solution()
print(sol.canCompleteCircuit([3, 1, 1], [1, 2, 2]))
