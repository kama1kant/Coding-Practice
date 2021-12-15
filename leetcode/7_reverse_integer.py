from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        
        reverse = 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse * sign if reverse < pow(2, 31) else 0
        
sol = Solution()
output = sol.reverse(-128)
print(output)
