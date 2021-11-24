from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def add(exp, cur):
            nonlocal ans
            if(exp+1 == cur):
                ans.append(str(exp))
            else:
                ans.append(str(exp) + '->' + str(cur-1))

        ans = []
        exp = lower

        if len(nums) == 0:
            add(lower, upper+1)
            return ans

        for e in nums:
            if e > exp:
                add(exp, e)
            exp = e+1

        if nums[len(nums)-1] < upper:
            add(nums[len(nums)-1]+1, upper+1)
        return ans


sol = Solution()
output = sol.findMissingRanges([], -1, -1)
print(output)
