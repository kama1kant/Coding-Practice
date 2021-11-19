class Solution:
    def solveNQueens(self, n):
        ans = []
        board = [[]]
        board = [['.' for i in range(n)] for j in range(n)]
        row_container, col_container, diag_container, anti_diag_container = [], [], [], []
        
        def create_board():
            arr = []
            for i in range(len(board)):
                row = ''
                for j in range(len(board[0])):
                    row += board[i][j]
                arr.append(row)
            ans.append(arr)
        
        def backtrack(row):
            output = False
            if(row >= n):
                create_board()
                output = True
                
            for col in range(n):
                if(row not in row_container and col not in col_container
                   and (row-col) not in diag_container and (row+col) not in anti_diag_container):
                    board[row][col] = 'Q'
                    row_container.append(row)
                    col_container.append(col)
                    diag_container.append(row-col)
                    anti_diag_container.append(row+col)
                    output = backtrack(row+1)
                    
                    board[row][col] = '.'
                    row_container.remove(row)
                    col_container.remove(col)
                    diag_container.remove(row-col)
                    anti_diag_container.remove(row+col)
                        
            return output
        
        backtrack(0)
        return(ans)
        
sol = Solution()
board = sol.solveNQueens(4)
print(board)