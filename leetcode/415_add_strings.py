class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        ans, carry, i, j = '', 0, len(num1)-1, len(num2)-1

        while i >= 0 or j >= 0:
            v1 = ord(num1[i])-ord('0')
            v2 = ord(num2[j])-ord('0') if j >= 0 else 0
            total = v1 + v2 + carry
            carry, ans, i, j = total//10, str(total % 10) + ans, i-1, j-1

        ans = ans if carry <= 0 else str(carry)+ans
        return ans


sol = Solution()
print(sol.addStrings('11', '119'))