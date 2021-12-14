from typing import List
import bisect

class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        print(dp)
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        sub.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                j = bisect.bisect_left(sub, nums[i])
                sub[j] = nums[i]

        print(sub)
        return len(sub)

        
        
        

sol = Solution()
output = sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
print(output)