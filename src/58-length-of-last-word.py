from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        reset = False
        for i in range(len(s)):
            if(s[i] != ' '):
                if(reset):
                    length = 0
                    reset = False
                length += 1
            else:
                reset = True
            
        return length
        
            
sol = Solution()
ans = sol.lengthOfLastWord("Hello World")
print(ans)