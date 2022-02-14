class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        num, i, n = 0, 0, len(s)

        while i < n:
            if(i+1 < n and s[i]+s[i+1] in dict):
                num += dict[s[i]+s[i+1]]
                i += 2
            else:
                num += dict[s[i]]
                i += 1

        return num

sol = Solution()
sol.romanToInt('IV')