from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markIslands(i, j):
            nonlocal grid
            if((i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0]))):
                return 
            if grid[i][j] == "1":
                grid[i][j] = "."
                markIslands(i-1, j)
                markIslands(i+1, j)
                markIslands(i, j-1)
                markIslands(i, j+1)
                        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    markIslands(i, j)
                    count += 1

        return count

sol = Solution()
output = sol.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
print(output)