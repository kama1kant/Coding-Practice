from typing import List

class Solution:
    def setZeroes(self, matrix):
        is_row = is_col = False
        for j in range(len(matrix[0])):
            if(matrix[0][j] == 0):
                is_row = True
        for i in range(len(matrix)):
            if(matrix[i][0] == 0):
                is_col = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if(matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if(is_row):
                matrix[0][j] = 0
        for i in range(len(matrix)):
            if(is_col):
                matrix[i][0] = 0
                
        return matrix
        
sol = Solution()
output = sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
print(output)