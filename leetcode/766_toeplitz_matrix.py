class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m-1):
            prev_i, j = i, 0
            v = matrix[i][j]
            
            while i < m and j < n:
                if matrix[i][j] != v:
                    return False
                j, i = j+1, i+1
            
            i = prev_i
            
        for j in range(n-1):
            prev_j, i = j, 0
            v = matrix[i][j]
            
            while i < m and j < n:
                if matrix[i][j] != v:
                    return False
                j, i = j+1, i+1
            
            j = prev_j
        
        return True