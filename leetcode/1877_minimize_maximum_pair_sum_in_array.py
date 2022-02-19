from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums, n, ans = sorted(nums), len(nums), float(-inf)
        for i in range(n//2):
            ans = max(ans, nums[i]+nums[n-1-i])
        
        return ans
    
    
sol = Solution()
print(sol.minPairSum([3,5,2,3]))
print(sol.minPairSum([3,5,4,2,4,6]))