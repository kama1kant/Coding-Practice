from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n, count = len(matrix), len(matrix[0]), 0

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        count += 1
                    else:
                        matrix[i][j] = min(
                            matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                        count += matrix[i][j]
        return count


sol = Solution()
print(sol.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
print(sol.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
print(sol.countSquares([[1]]))