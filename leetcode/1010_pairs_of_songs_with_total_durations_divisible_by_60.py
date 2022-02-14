from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dur, count = 60, 0
        hash = {i: [] for i in range(dur)}

        for i, t in enumerate(time):
            mod = t % dur
            rem = 0 if mod == 0 else dur - mod
            v = hash[rem]
            count += len(v)

            hash[t % dur].append(i)

        return count


sol = Solution()
print(sol.numPairsDivisibleBy60([30,20,150,100,40]))
print(sol.numPairsDivisibleBy60([60,60,60]))
print(sol.numPairsDivisibleBy60(
    [418, 204, 77, 278, 239, 457, 284, 263, 372, 279, 476, 416, 360, 18]))
