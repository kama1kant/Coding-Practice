from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans, dp = 0, [False for i in range((len(s)+1))]
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if s[i:j] in wordDict and dp[i]:
                    dp[j] = True
        
        return dp[-1]

        
sol = Solution()
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(sol.wordBreak("applepenapple", ["apple","pen"]))
print(sol.wordBreak("abcd", ["a","abc","b","cd"]))
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))