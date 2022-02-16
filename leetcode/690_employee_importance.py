"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        que, hashmap, ans = [id], collections.defaultdict(list), 0

        for e in employees:
            hashmap[e.id] = e

        while len(que) > 0:
            id = que.pop(0)
            ans += hashmap[id].importance
            que += hashmap[id].subordinates

        return ans


sol = Solution()
print(sol.getImportance([[1,5,[2,3]],[2,3,[]],[3,3,[]]], 1))
print(sol.getImportance([[1,2,[5]],[5,-3,[]]], 5))