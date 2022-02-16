from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = self.nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            id = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[id] = self.nums[id], self.nums[i]
        return self.nums


sol = Solution([1, 2, 3])
print(sol.shuffle())
print(sol.reset())
print(sol.shuffle())