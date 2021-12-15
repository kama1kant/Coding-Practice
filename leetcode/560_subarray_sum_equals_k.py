from typing import List


class Solution:
    # Approach 1
    def subarraySum1(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if(sum == k):
                    count += 1
        return count
    
    # Approach 2
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_arr = {}
        curr_sum = 0
        for i in range(len(nums)):
            print(curr_sum, sum_arr)
            curr_sum += nums[i]
            if curr_sum == k:
                count += 1
            if (curr_sum - k) in sum_arr:
                count += sum_arr[curr_sum - k]
                
            if curr_sum in sum_arr:
                sum_arr[curr_sum] += 1
            else:
                sum_arr[curr_sum] = 1
                
        return count
        
sol = Solution()
output = sol.subarraySum([1, 1, 1], 2)
print(output)