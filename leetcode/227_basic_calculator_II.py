from typing import List
import random

class Solution:        
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isnumeric():
                num = num * 10 + int(s[i])
            if i == len(s) - 1 or (not s[i].isnumeric() and s[i] != ' '):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # stack.append(floor(stack.pop() / num))
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp % num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
            
            print(s[i], stack, num, sign)
            
        return sum(stack)
            

sol = Solution()
output = sol.calculate("14-3/2")
print(output)