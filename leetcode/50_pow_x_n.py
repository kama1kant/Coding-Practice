class Solution:    
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        elif n == 0:
            return 1
            
        i, pow, mul = 1, 1, x
        while i <= n:
            print(i, mul, pow)
            if i == n:
                break
            elif i*2 <= n:
                mul *= mul
                i = i*2
            else:
                pow *= mul
                mul = x
                i += 1
        return pow*mul
        

sol = Solution()
print(sol.myPow(0.00001, 2147483647))
