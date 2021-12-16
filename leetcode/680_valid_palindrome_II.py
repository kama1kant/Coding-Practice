class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        isSkipped = False
        
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            elif not isSkipped:
                isSkipped = True
                substr1 = s[start:end]
                substr2 = s[start+1:end+1]
                
                if substr1 == substr1[::-1] or substr2 == substr2[::-1]:
                    return True
                else:
                    return False
            else:
                return False
        
        return True
            

sol = Solution()
output = sol.validPalindrome("ebcbbececabbacecbbcbe")
print(output)