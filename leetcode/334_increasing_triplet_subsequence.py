from typing import List
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = math.inf
        for i in range(len(nums)):
            if(nums[i] <= num1):
                num1 = nums[i]
            elif(nums[i] <= num2):
                num2 = nums[i]
            else:
                return True
                       
            print(num1, num2)
        return False


sol = Solution()
output = sol.increasingTriplet([20,100,10,12,6,5,13])
print(output)