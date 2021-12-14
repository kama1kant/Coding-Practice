from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency_arr = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        for key in hashmap:
            frequency_arr[hashmap[key]].append(key)
        
        ans = []
        i = len(nums)
        while k > 0:
            if(len(frequency_arr[i]) > 0):
                for num in frequency_arr[i]:
                    if(k <= 0):
                        break
                    ans.append(num)
                    k -= 1
                    
            i -= 1
        
        return ans
    

sol = Solution()
output = sol.topKFrequent([-1, -1], 1)
print(output)