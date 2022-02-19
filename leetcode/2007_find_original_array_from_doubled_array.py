from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        length = len(changed)
        if length % 2 != 0:
            return []
        changed, hashmap, ans = sorted(changed), {}, []

        for i in range(len(changed)):
            n = changed[i]
            if n in hashmap and hashmap[n] > 0:
                ans.append(n//2)
                hashmap[n] -= 1
            else:
                if n*2 not in hashmap:
                    hashmap[n*2] = 0
                hashmap[n*2] += 1
        return ans if len(ans) == length//2 else []


sol = Solution()
print(sol.findOriginalArray([1, 3, 4, 2, 6, 8]))
print(sol.findOriginalArray([6, 3, 0, 1]))
print(sol.findOriginalArray([1]))
print(sol.findOriginalArray([0, 0, 0, 0]))
print(sol.findOriginalArray([2, 1, 2, 4, 2, 4]))
print(sol.findOriginalArray([3, 3, 3, 3]))