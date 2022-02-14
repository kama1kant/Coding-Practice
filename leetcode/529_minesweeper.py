from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def isValidPos(pos):
            return True if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]) else False
        
        queue = []
        dir = [[0,-1], [-1,0], [0,1], [1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
        
        if board[click[0]][click[1]] == 'E':
            queue.append([click[0],click[1]])
            board[click[0]][click[1]] = 'B'
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        
        while len(queue) > 0:
            pos = queue.pop(0)
            count = 0
            for d in dir:                
                newPos = [pos[0]+d[0], pos[1]+d[1]]
                if isValidPos(newPos):
                    if board[newPos[0]][newPos[1]] == 'M':
                        count += 1
            if count > 0:
                board[pos[0]][pos[1]] = str(count)
            else:
                for d in dir:                
                    newPos = [pos[0]+d[0], pos[1]+d[1]]

                    if isValidPos(newPos):
                        # print(newPos, d, queue)
                        if board[newPos[0]][newPos[1]] == 'E':
                            queue.append([newPos[0],newPos[1]])
                            board[newPos[0]][newPos[1]] = 'B'
        
        return board


sol = Solution()
print(sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3,0]))
print(sol.updateBoard([["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], [1,2]))
print(sol.updateBoard([["E","M","M","E","E","E","E","E"],["E","E","M","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","M","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"]], [5,5]))
print(sol.updateBoard([["E"]], [0,0]))