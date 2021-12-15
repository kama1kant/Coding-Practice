from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
            l, h = 0, len(nums)-1
            while l <= h:
                mid = (l+h)//2
                print(l, mid, h)
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    if target > nums[h] and nums[mid] < nums[l]:
                        h = mid - 1
                    else:
                        l = mid + 1
                else:
                    if target < nums[l]:
                        l = mid + 1
                    else:
                        h = mid - 1
            
            return -1
                                

sol = Solution()
output = sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8)
print(output)