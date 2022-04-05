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


# New
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         if len(nums) == 0:
#             return nums

#         j, k = -1, -1
#         for i in range(len(nums)-1):
#             if nums[i] < nums[i+1]:
#                 j, k = i, i+1
#             if j != -1 and nums[i+1] > nums[j] and nums[i+1] < nums[k]:
#                 k = i+1

#         if j == -1 and k == -1:
#             return sorted(nums)
#         else:
#             nums[j], nums[k] = nums[k], nums[j]
#             return nums[:j+1] + sorted(nums[j+1:])


# sol = Solution()
# print(sol.nextPermutation([1, 2, 5, 4, 3]))
# print(sol.nextPermutation([3, 2, 1]))
# print(sol.nextPermutation([3, 1, 2]))
