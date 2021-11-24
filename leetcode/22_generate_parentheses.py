from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(bag, open_count, close_count):
            nonlocal n
            if len(bag) == n*2:
                ans.append("".join(bag))
                return

            if open_count < n:
                bag.append('(')
                backtrack(bag, open_count+1, close_count)
                bag.pop()
            if close_count < open_count:
                bag.append(')')
                backtrack(bag, open_count, close_count+1)
                bag.pop()

        backtrack([], 0, 0)
        return ans
    
sol = Solution()
output = sol.generateParenthesis(3)
print(output)