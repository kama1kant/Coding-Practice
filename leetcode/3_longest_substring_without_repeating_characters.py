from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        max_len = start = 0
        
        for i in range(len(s)):
            if s[i] in hash:
                start = hash[s[i]]+1 if hash[s[i]] >= start else start
            hash[s[i]] = i
            
            max_len = max(max_len, (i-start)+1)
        return max_len
        
        
sol = Solution()
output = sol.lengthOfLongestSubstring("abcabcbb")
print(output)
