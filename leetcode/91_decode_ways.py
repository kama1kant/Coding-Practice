class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0

        def backtrack(i):
            nonlocal s, ans

            if i == len(s):
                ans += 1
                return
            elif i < len(s) and int(s[i]) > 0:
                backtrack(i+1)
                if i < len(s)-1 and 1 <= int(s[i]+s[i+1]) <= 26:
                    backtrack(i+2)

        backtrack(0)
        return ans
