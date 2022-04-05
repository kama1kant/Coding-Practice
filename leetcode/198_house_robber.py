class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prev1, prev2 = nums[0], 0
        for i in range(1, len(nums)):
            prev2 = max(prev1, prev2+nums[i])
            prev2, prev1 = prev1, prev2
        return prev1