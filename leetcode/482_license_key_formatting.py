from typing import List


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans, s, temp = [], s.replace('-', '').upper(), ''
        i = len(s)-1

        while i >= 0:
            if len(temp) > 0 and len(temp) % k == 0:
                ans.append(temp)
                temp = ''
            temp = s[i] + temp
            i -= 1

        if len(temp) > 0:
            ans.append(temp)
        return '-'.join(ans[::-1])


sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(sol.licenseKeyFormatting("2-5g-3-J", 2))