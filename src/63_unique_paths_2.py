from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        is_first_row_obstacle = False
        is_first_col_obstacle = False
        if(obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1):
            return 0
        
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        # for j in range(n):
        #     if(obstacleGrid[0][j] == 1):
        #         is_first_row_obstacle = True
        
        # for i in range(m):
        #     if(obstacleGrid[i][0] == 1):
        #         is_first_col_obstacle = True
        
        print(obstacleGrid)
        for i in range(m):
            for j in range(n):
                if(obstacleGrid[i][j] == 1 or (i == 0 and is_first_row_obstacle) or (j == 0 and is_first_col_obstacle)):
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if(obstacleGrid[i][j] == 0):
                    continue
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1]
        
sol = Solution()
ans = sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
print(ans)