from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtrack(bag, _nums):
            nonlocal n
            if len(bag) == n:
                ans.append(bag.copy())
                return

            for i in range(len(_nums)):
                bag.append(_nums[i])
                temp_nums = _nums.copy()
                _nums.remove(_nums[i])
                
                backtrack(bag, _nums)
                
                bag.pop()
                _nums = temp_nums.copy()
            
        backtrack([], nums)
        return ans
    
sol = Solution()
output = sol.permute([1, 2, 3])
print(output)