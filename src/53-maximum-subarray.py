from typing import List
import math


# Approach 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        temp_sum = 0
        for i in range(len(nums)):
            temp_sum = max(temp_sum+nums[i], nums[i])
            max_sum = max(max_sum, temp_sum)
        
        return(max_sum)
            

sol = Solution()
board = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(board)


# Approach 1
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -math.inf
#         for i in range(len(nums)):
#             temp_sum = 0
#             for j in range(i, len(nums)):
#                 temp_sum += nums[j]
#                 max_sum = max(max_sum, temp_sum)
        
#         return(max_sum)
            

# sol = Solution()
# board = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# print(board)