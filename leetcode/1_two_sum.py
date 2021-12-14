from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashmap and hashmap[remainder] != i:
                return [i, hashmap[remainder]]
            
            hashmap[nums[i]] = i
        
        
sol = Solution()
output = sol.twoSum([3, 3], 6)
print(output)
