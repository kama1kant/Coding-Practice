class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {'(':')', '{':'}', '[': ']'}
        for i in range(len(s)):
            print(s[i], stack)
            if s[i] in bracket_map:
                stack.append(s[i])
            else:
                if len(stack) <= 0:
                    return False
                
                item = stack.pop()
                
                if bracket_map[item] != s[i]:
                    return False
                
        return len(stack) == 0
                
        
        
sol = Solution()
output = sol.isValid("()")
print(output)