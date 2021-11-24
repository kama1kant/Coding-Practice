# Approach 2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if(m <=0 or n <= 0):
            return 0
        board = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        
        return board[m-1][n-1]
        
sol = Solution()
ans = sol.uniquePaths(3, 2)
print(ans)




# Approach 1
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         output = 0
#         def backtrack(row, col):
#             nonlocal output, m, n
            
#             if(row == m-1 and col == n-1):
#                 output += 1
            
#             if(row >= m or col >= n):
#                 return 0

#             backtrack(row, col+1)
#             backtrack(row+1, col)
            
#         backtrack(0, 0)
#         return output
        
# sol = Solution()
# ans = sol.uniquePaths(0, 0)
# print(ans)