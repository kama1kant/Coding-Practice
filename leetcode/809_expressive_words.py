from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def getRepeatedLength(w, i):
            if i >= len(w):
                return 0
            
            c = w[i]
            count = 0
            while i < len(w):
                if w[i] != c:
                    break
                else:
                    count += 1
                    i += 1
            return count
        
        def check(w):
            i = 0
            j = 0
            
            while i < len(s) and j < len(w):
                if s[i] != w[j]:
                    return False
                
                len1 = getRepeatedLength(s, i)
                len2 = getRepeatedLength(w, j)
                
                i = i + len1
                j = j + len2
                
                if len1 != len2:
                    if len1 < len2 or len2 == 0 or len1 < 3:
                        print(w)
                        print(i, j, len1, len2)
                        return False
            
            if i == len(s) and j == len(w):
                return True
            else:
                return False
        
        count = 0
        for w in words:
            ans = check(w)
            count = count + 1 if ans else count
        return count
                        
            
sol = Solution()
output = sol.expressiveWords("heeellooo", ["heeelloooworld"])
print(output)