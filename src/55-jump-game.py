from typing import List

# Approach 2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums)-1        
        
        for i in range(len(nums)-2, -1, -1):
            if(i+nums[i] >= last_pos):
                last_pos = i
        
        return(last_pos == 0)
            
        
sol = Solution()
ans = sol.canJump([2,3,1,1,4])
print(ans)







# Approach 1
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def backtrack(nums, i):
#             if(i >= (len(nums)-1)):
#                 return True
            
#             farthest = min(nums[i], len(nums)-1)
#             for j in range(farthest, 0, -1):
#                 output = backtrack(nums, i+j)
#                 if(output):
#                     return True
            
#             return False
         
#         return backtrack(nums, 0)        
        
# sol = Solution()
# ans = sol.canJump([0])
# print(ans)