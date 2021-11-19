from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traverse = [[0,1],[1,0],[0,-1],[-1,0]]
        ans = []
        i = row = col = total_print = 0
        
        while(total_print < (len(matrix) * len(matrix[0]))):
            ans.append(matrix[row][col])
            matrix[row][col] = '#'
            total_print += 1
            
            if(row+traverse[i][0] >= len(matrix) or col+traverse[i][1] >= len(matrix[0]) or matrix[row+traverse[i][0]][col+traverse[i][1]] == '#'):
                i = (i+1)%4
            
            row += traverse[i][0]
            col += traverse[i][1]            
            
        return ans
                
        
sol = Solution()
ans = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(ans)