from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        obj = {}
        for ele in strs:
            count = [0] * 26
            for c in ele:
                count[ord(c)-97] += 1
            
            key = '-'.join(str(e) for e in count)
    
            if key not in obj:
                obj[key] = []
            obj[key].append(ele)
        
        ans = []
        for key in obj:
            ans.append(obj[key])
                    
        return ans
        
        
sol = Solution()
output = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(output)