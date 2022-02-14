from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(arr, target):
            # print(target)
            ans = []
            l, h = 0, len(arr)-1
            while l < h:
                if arr[l] + arr[h] < target:
                    l += 1
                elif arr[l] + arr[h] > target:
                    h -= 1
                else:
                    ans.append([arr[l], arr[h]])
                    l += 1
                    h -= 1
            return ans
        
        n, k, nums, ans = len(nums), 4, sorted(nums), []
        # print(nums)
        def backtrack(arr, total):
            nonlocal nums, n, k, target, ans
            avg = target//k
            
            if len(arr) == k-2:
                res = [nums[i] for i in arr]
                twoArr = nums[arr[-1]+1:]
                # print(res, nums[arr[-1]+1:], target-sum(res), sum(res))
                if len(twoArr) > 0 and avg >= twoArr[0] and avg <= twoArr[-1]:
                    twos = twoSum(twoArr, target-total)
                    for two in twos:
                        ans.append(res+two) if res+two not in ans else None 
                
            for i in range(arr[-1]+1, n):
                arr.append(i)
                total += nums[i]
                
                backtrack(arr, total)
                arr.remove(i)
                total -= nums[i]
        
        for i in range(n):
            backtrack([i], nums[i])
        return ans
        
        
sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))
print(sol.fourSum([2,2,2,2,2], 8))
print(sol.fourSum([0,0,0,0], 0))
print(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0))
print(sol.fourSum([1,-2,-5,-4,-3,3,3,5], -11))