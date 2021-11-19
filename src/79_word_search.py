class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            row = []
            for j in range(len(board[0])):
                row.append(board[i][j])
            print(row)

        output = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                output = self.backtrack(board, word, i, j)
                if(output):
                    return output
        return output

    def backtrack(self, board, word, row, col):
        if(len(word) == 0):
            return True
        
        if(row < 0 or row >= len(board) or col < 0 
           or col >= len(board[0] or board[row][col] != word[0])):
            return False
        
        if(board[row][col] == word[0]):
            old_val = board[row][col]
            board[row][col] = "#"
            iterate = [[0,1], [1,0], [0,-1], [-1,0]]
            output = False
            for val in iterate:
                output = self.backtrack(board, word[1:], row+val[0], col+val[1])
                if(output):
                    return True
            
            if(output == False):
                board[row][col] = old_val
        return False

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
output = sol.exist(board, word)
print(output)