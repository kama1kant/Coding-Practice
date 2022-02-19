from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = []
        for e in emails:
            [e, d] = e.split('@')
            e = e.split('+')[0]
            e = e.replace('.', '')
            if e+'@'+d not in ans:
                ans.append(e+'@'+d)
        print(ans)
        return len(ans)


sol = Solution()
sol.numUniqueEmails(["test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])