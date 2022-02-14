from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        ans, per, arr = 0, [], [i for i in range(1, n+1)]

        def backtrack(arr, per):
            nonlocal ans, n
            if len(per) >= n:
                print(per)
                ans += 1
                return

            for i in range(len(arr)):
                val, index = arr[i], len(per)+1
                if index % val == 0 or val % index == 0:
                    copy = arr.copy()
                    per.append(val)
                    arr.remove(val)

                    backtrack(arr, per)

                    arr = copy.copy()
                    per.remove(val)

        backtrack(arr, per)
        return ans


sol = Solution()
print(sol.countArrangement(2))
