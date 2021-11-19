from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)-1
        n = len(grid[0])-1
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if(i == m and j != n):
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                elif(i != m and j == n):
                    grid[i][j] = grid[i][j] + grid[i+1][j]
                elif(i == m and j == n):
                    continue
                else:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])
                
        return (grid[0][0])
     
            
sol = Solution()
ans = sol.minPathSum([[1,2,3],[4,5,6]])
print(ans)