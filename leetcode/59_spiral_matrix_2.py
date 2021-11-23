from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [['#' for j in range(n)] for i in range(n)]
        traverse = [[0,1], [1,0], [0,-1], [-1,0]]
        total_elements = n*n
        cur_element = 1
        row = col = i = 0
        
        while(cur_element < total_elements+1):
            matrix[row][col] = cur_element
            cur_element += 1
            row += traverse[i][0]
            col += traverse[i][1]
            
            if(row >= n or col >= n or matrix[row][col] != '#'):
                row -= traverse[i][0]
                col -= traverse[i][1]
                
                i = (i+1)%4
                
                row += traverse[i][0]
                col += traverse[i][1]
        return matrix
        
sol = Solution()
ans = sol.generateMatrix(3)
print(ans)