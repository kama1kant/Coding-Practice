class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j, ans = 0, 0, []

        while i < len(firstList) and j < len(secondList):
            f0, f1, s0, s1 = firstList[i][0], firstList[i][1], secondList[j][0], secondList[j][1]

            if s0 <= f1 <= s1 or f0 <= s1 <= f1:
                ans.append([max(f0, s0), min(f1, s1)])
            if f1 >= s1:
                j += 1
            else:
                i += 1

        return ans