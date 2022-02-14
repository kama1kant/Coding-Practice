from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        def insertNumeral(chars, c, pos, num):
            numStr, i = '', 0
            chars[pos-1] = c
            
            if int(num) <= 1:
                return pos
        
            while int(num) > 0:
                v = num%10
                num //= 10
                numStr += str(v)
                
            numStr = numStr[::-1]
            while i < len(numStr):
                chars[pos] = numStr[i]
                pos += 1
                i += 1
            return pos
                
        prevc, previ, pos = chars[0], 0, 0
        chars.append(-1)
        
        for i in range(1, len(chars)):
            
            if prevc != chars[i]:
                pos = insertNumeral(chars, prevc, pos+1, i - previ)
                
                if chars[i] == -1:
                    break
                prevc = chars[i]
                previ = i
        
        print(chars[:pos], pos)
        return pos
        

sol = Solution()
print(sol.compress(["a"]))
print(sol.compress(["a","a","b","b","c","c","c"]))
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(sol.compress(["a","a","a","b","b","a","a"]))
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","a"]))