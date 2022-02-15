class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        ans, val = '', list(dict.keys())

        while num > 0:
            i = bisect.bisect_left(val, num)
            if i < len(val) and num == val[i]:
                v = val[i]
            else:
                v = val[i-1]

            num -= v
            ans += dict[v]

        return ans


sol = Solution()
print(sol.intToRoman(3))
print(sol.intToRoman(58))
print(sol.intToRoman(1994))
