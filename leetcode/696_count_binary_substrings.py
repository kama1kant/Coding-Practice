from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        a, b, count, lasta, isLastB = 1, 0, 0, int(s[0]), False
        lastb = lasta ^ 1

        for i in range(1, len(s)):
            if isLastB and lastb != int(s[i]):
                count += min(a, b)
                a = b
                b = 0
                lasta = lasta ^ 1
                lastb = lastb ^ 1

            if lasta == int(s[i]):
                a += 1
            elif lastb == int(s[i]):
                b += 1
                isLastB = True

        count += min(a, b)
        return count


sol = Solution()
print(sol.countBinarySubstrings("00110011"))
print(sol.countBinarySubstrings("01"))
print(sol.countBinarySubstrings("10101"))
