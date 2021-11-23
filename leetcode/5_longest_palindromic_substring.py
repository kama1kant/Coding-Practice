from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def scan(l, r):
            nonlocal s
            cur_len = 1
            if(l<0 or r>len(s)-1):
                return cur_len;
            
            if(s[l] != s[r]):
                return cur_len;
            
            while(l>=0 and r<=len(s)-1 and s[l] == s[r]):
                cur_len = (r-l+1)
                l -= 1
                r += 1
                
            return cur_len
        
        start = max_len = 0
        for i in range(len(s)):
            len1 = scan(i, i)
            len2 = scan(i, i+1)
            cur_len = max(len1, len2)
            
            if(cur_len > max_len):
                max_len = cur_len
                start = i - (cur_len-1)//2
        
        return s[start:start+max_len]
        
        
        
        
sol = Solution()
output = sol.longestPalindrome("adabbafds")
print(output)