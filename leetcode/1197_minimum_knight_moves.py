from typing import List

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        moves = [[2, 1], [1, 2], [-2, 1], [-1, 2], [2, -1], [1, -2], [-2, -1], [-1, -2]]
        ans, step, visited, queue, counter = float(inf), 0, [], [[0,0]], {'0-0': 0}
        
        while len(queue) > 0:
            [i, j] = queue.pop(0)
            step += 1
            for m in moves:
                newi, newj = i+m[0], j+m[1]
                if newi == x and newj == y:
                    ans = min(ans, counter[str(i) + '-' + str(j)] + 1)
                if newi >= 0 and newj >= 0 and newi-x <= 2 and newj-y <= 2 and [newi, newj] not in visited:
                    visited.append([newi, newj])
                    queue.append([newi, newj])
                    counter[str(newi) + '-' + str(newj)] = counter[str(i) + '-' + str(j)] + 1
                print(queue)
        return ans
        
        
sol = Solution()
print(sol.minKnightMoves(1,1))