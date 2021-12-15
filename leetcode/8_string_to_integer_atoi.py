class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        has_digit_started = False
        ans = 0
        
        for i in range(len(s)):
            if not has_digit_started and (s[i] == '-' or s[i] == '+'):
                has_digit_started = True
                if s[i] == '-':
                    sign = -1
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
                if not has_digit_started:
                    has_digit_started = True
                ans = (ans * 10) + (ord(s[i]) - 48)
            elif not has_digit_started and ord(s[i]) == 32:
                continue
            else:
                break
        
        ans *= sign
        if ans > (pow(2, 31) - 1):
            ans = pow(2, 31) - 1
        elif ans < pow(-2, 31):
            ans = pow(-2, 31)
        
        return ans
        
        
sol = Solution()
output = sol.myAtoi(" -+9")
print(output)
