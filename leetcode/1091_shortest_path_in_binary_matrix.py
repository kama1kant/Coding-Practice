class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, dirc = len(grid), [[1, 1], [0, 1], [1, 0],
                              [-1, -1], [0, -1], [-1, 0], [1, -1], [-1, 1]]

        def bfs():
            nonlocal dirc, n
            q, step, i, j = [], 1, 0, 0
            grid[i][j] = 1
            q.append([i, j, step])

            while len(q) > 0:
                print(q)
                [q_i, q_j, step] = q.pop(0)
                for d in dirc:
                    i, j = q_i+d[0], q_j+d[1]
                    if i >= 0 and j >= 0 and i < n and j < n and grid[i][j] == 0:
                        grid[i][j] = 1
                        if i == n-1 and j == n-1:
                            print('hello', step)
                            return step+1
                        else:
                            q.append([i, j, step+1])
            print(q)
            return -1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            print('hello2 ', step)
            return -1
        else:
            return bfs()


sol = Solution()
# print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]]))
# print(sol.shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))
# print(sol.shortestPathBinaryMatrix([[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]))
print(sol.shortestPathBinaryMatrix([[0]]))
