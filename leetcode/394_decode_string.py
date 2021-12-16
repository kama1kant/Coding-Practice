class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':                
                ret = ''
                count = 1
                for i in range(len(stack)):
                    c = stack.pop()
                    if c.isnumeric():
                        temp = c
                        while len(stack) > 0 and stack[-1].isnumeric():
                            c = stack.pop()
                            temp = c + temp
                            
                        count = int(temp)
                        break
                    elif c != '[':
                        ret = c + ret
                
                stack.append(ret * count)
            else:
                stack.append(s[i])
        print(stack)
        
        ans = ""
        for ele in stack:
            ans += ele
        
        return ans                    
                    
                    

sol = Solution()
output = sol.decodeString("10[a]")
print(output)