from typing import List
import random

class Solution:
    def __init__(self, w: List[int]):
        self.sum_arr = []
        self.total_sum = 0
        self.w = w
        for ele in w:            
            self.total_sum += ele
            self.sum_arr.append(self.total_sum)

    def pickIndex1(self) -> int:
        offset = self.total_sum * random.random()
        for i in range(len(self.sum_arr)):
            if offset < self.sum_arr[i]:
                return i
            
    def pickIndex(self) -> int:
        offset = self.total_sum * random.random()
        l, h = 0, len(self.sum_arr)-1
        while l < h:
            mid = (l+h)//2
            if self.sum_arr[mid] > offset and self.sum_arr[mid-1] < offset:
                return mid
            elif self.sum_arr[mid] < offset:
                l = mid+1
            else:
                h = mid-1
                
        return l
            

sol = Solution([1, 3])
for i in range(20):
    output = sol.pickIndex()
    print(output)