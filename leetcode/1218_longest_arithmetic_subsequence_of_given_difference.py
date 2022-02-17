class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap, ans = {}, 1
        
        for n in arr:
            print(hashmap)
            if n-difference in hashmap:
                hashmap[n] = hashmap[n-difference] + 1
            else:
                hashmap[n] = 1
            if hashmap[n] > ans: ans = hashmap[n]
        return ans
        
sol = Solution()
print(sol.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))