from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        arr = sorted(arr, key=lambda x:abs(x))
        
        for n in arr:
            if count[n] > 0:
                if count[2*n] <= 0:
                    return False
                else:
                    count[n] -= 1
                    count[2*n] -= 1
        return True
        
sol = Solution()
print(sol.canReorderDoubled([4,-2,2,-4]))
print(sol.canReorderDoubled([3,1,3,6]))
print(sol.canReorderDoubled([2,1,2,6]))
print(sol.canReorderDoubled([1,2,4,16,8,4]))