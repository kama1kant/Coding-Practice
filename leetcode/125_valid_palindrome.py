class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        for c in s:
            if c.isalpha():
                c = c.lower()
                ans += c
            elif c.isnumeric():
                ans += c
        return ans == ans[::-1]
