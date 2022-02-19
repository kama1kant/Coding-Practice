from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j, total, ans, hashmap = 0, 0, 0, 0, {}
        while i < len(fruits):
            if fruits[i] not in hashmap:
                hashmap[fruits[i]] = 0
            hashmap[fruits[i]] += 1

            while len(list(hashmap.keys())) > 2:
                hashmap[fruits[j]] -= 1
                if hashmap[fruits[j]] == 0:
                    del hashmap[fruits[j]]
                j += 1

            i += 1
            ans = max(ans, sum(list(hashmap.values())))
        return ans


sol = Solution()
print(sol.totalFruit([1,2,1]))
print(sol.totalFruit([0,1,2,2]))
print(sol.totalFruit([1, 2, 3, 2, 2]))
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
print(sol.totalFruit([1,0,1,4,1,4,1,2,3]))