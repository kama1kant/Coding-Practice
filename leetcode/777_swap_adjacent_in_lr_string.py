from typing import List


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        hs, he = [], []
        for i in range(len(start)):
            if start[i] != 'X':
                hs.append([start[i], i])
            if end[i] != 'X':
                he.append([end[i], i])

        n = len(hs)
        if n != len(he):
            return False

        for i in range(n):
            if hs[i][0] != he[i][0]:
                return False
            if hs[i][0] == 'L' and hs[i][1] < he[i][1]:
                return False
            if hs[i][0] == 'R' and hs[i][1] > he[i][1]:
                return False
        return True


sol = Solution()
print(sol.canTransform("RXXLRXRXL", "XRLXXRRLX"))
print(sol.canTransform("X", "R"))
print(sol.canTransform("RL", "LR"))
print(sol.canTransform("LXXLXRLXXL", "XLLXRXLXLX"))
print(sol.canTransform("XXXXXLXXXX", "LXXXXXXXXX"))