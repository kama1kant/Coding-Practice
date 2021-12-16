from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        return heapq.nlargest(k, nums)[-1]

sol = Solution()
output = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(output)
