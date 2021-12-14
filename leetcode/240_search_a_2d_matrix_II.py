from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_ptr = len(matrix) - 1
        c_ptr = 0
        while r_ptr >= 0 and c_ptr < len(matrix[0]):
            print(r_ptr, c_ptr)
            if target > matrix[r_ptr][c_ptr]:
                c_ptr += 1
            elif target < matrix[r_ptr][c_ptr]:
                r_ptr -= 1
            else:
                return True
        
        return False

sol = Solution()
output = sol.searchMatrix([[-5]], -5)
print(output)