from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        flag = False
        for j in range(n, 0, -1):
            i = j-1
            for k in range(i+1, n):
                replace = 9999
                if nums[k] > nums[i] and nums[k] < replace:
                    replace = nums[k]
                    flag = True
            if flag == True:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                break
        
        if(i < n-1 and flag == True):
            t1 = nums[:i+1]
            t2 = nums[i+1:]
            t2.sort()
            t1.extend(t2)
            nums = t1
        
        if(flag == False):
            nums.sort()
        
        return nums

sol = Solution()
nums = sol.nextPermutation([1,3,2])
print(nums)