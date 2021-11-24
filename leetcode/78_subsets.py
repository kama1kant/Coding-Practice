from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])

        def backtrack(bag, j, n):
            nonlocal nums
            if len(bag) == n:
                ans.append(bag.copy())
                return

            for i in range(j, len(nums)):
                bag.append(nums[i])
                backtrack(bag, i+1, n)
                bag.pop()

        for i in range(len(nums)):
            backtrack([], 0, i+1)
        return ans
    
    
    
sol = Solution()
output = sol.subsets([0])
print(output)