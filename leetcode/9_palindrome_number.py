class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        
        reverse = 0
        while(x//10 > reverse):
            reverse = (reverse * 10) + x % 10
            x //= 10
        
        print(x, reverse)
        
        return True if x == reverse or x//10 == reverse else False
        
sol = Solution()
output = sol.isPalindrome(10)
print(output)
