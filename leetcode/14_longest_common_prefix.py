from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_str = strs[0]
        for ele in strs:
            if len(ele) < len(smallest_str):
                smallest_str = ele
        strs.remove(smallest_str)
        
        for i in range(len(strs)):
            common = ''
            for j in range(len(smallest_str)):
                if strs[i][j] == smallest_str[j]:
                    common += smallest_str[j]
                else:
                    break
            smallest_str = common
        
        return smallest_str
                    
                  
sol = Solution()
output = sol.longestCommonPrefix(["cir", "car"])
print(output)