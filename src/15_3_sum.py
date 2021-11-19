from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            lo, hi = i+1, len(nums)-1
            while(lo<hi):
                if((nums[i] + nums[lo] + nums[hi]) == 0
                   and [nums[i], nums[lo], nums[hi]] not in ans):
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                elif((nums[i] + nums[lo] + nums[hi]) < 0):
                    lo += 1
                else:
                    hi -= 1
        
        return ans
        
        
sol = Solution()
output = sol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
print(output)