from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(isFirst):
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low+high)//2
                
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] == target:
                    if isFirst:
                        if mid == low or nums[mid-1] < target:
                            return mid
                        else:
                            high = mid - 1
                    else:
                        if mid == high or nums[mid+1] > target:
                            return mid
                        else:
                            low = mid + 1
            return -1
        
        first_bound = binarySearch(True)
        last_bound = binarySearch(False)

        return [first_bound, last_bound]
                    
                    
                

sol = Solution()
output = sol.searchRange([1, 1], 1)
print(output)