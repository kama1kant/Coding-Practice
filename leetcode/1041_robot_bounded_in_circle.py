from typing import List

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        face = 0
        
        def traverse():
            incrementer = [[0, 1], [-1, 0], [0, -1], [1, 0]]
            nonlocal face
            nonlocal pos
            
            for c in instructions:
                if c == 'L':
                    face = (face+1)%4
                elif c == 'R':
                    face = face-1 if face > 0 else 3
                else:
                    pos[0] += incrementer[face][0]
                    pos[1] += incrementer[face][1]
            return pos
        
        pos = traverse()
        
        if pos == [0, 0] or face != 0:
            return True
        else:
            return False


sol = Solution()
output = sol.isRobotBounded("GGLLGG")
print(output)
