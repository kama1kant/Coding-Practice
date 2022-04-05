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

# New
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s)-1
#         while i < j and s[i] == s[j]:
#             i += 1
#             j -= 1
#         if i < j:
#             one = s[:i] + s[i+1:]
#             two = s[:j] + s[j+1:]
#             return one == one[::-1] or two == two[::-1]
#         else:
#             return True

# sol = Solution()
# print(sol.validPalindrome('eededed'))