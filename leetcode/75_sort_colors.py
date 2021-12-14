from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums)-1
        cur = 0

        while(cur <= right):
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                cur += 1
            print(nums, left, right, cur)
        
        return nums

sol = Solution()
output = sol.sortColors([2, 0, 2, 1, 1, 0])
print(output)