from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        is_down = False
        cur_row = 0
        for i in range(len(s)):
            if cur_row >= numRows-1 or cur_row <= 0:
                is_down = not is_down
            
            rows[cur_row] += s[i]
            
            if is_down and cur_row + 1 < numRows:
                cur_row += 1
            elif not is_down and cur_row - 1 >= 0:
                cur_row -= 1
        
        print(rows)
        ans = ""
        for ele in rows:
            ans += ele

        return ans
        
        
sol = Solution()
output = sol.convert("PAYPALISHIRING", 3)
print(output)
