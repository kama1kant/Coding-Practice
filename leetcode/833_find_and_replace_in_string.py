from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        i, j, res = 0, 0, ''
        rep = sorted(list(zip(indices, sources, targets)), key=lambda x: x[0])
        indices, sources, targets = zip(*rep)
        
        while i < len(s):
            if j < len(indices) and i == indices[j]:
                if sources[j] == s[i:i+len(sources[j])]:
                    res += targets[j]
                    i += len(sources[j])
                else:
                    res += s[i]
                    i += 1
                j += 1
            else:
                res += s[i]
                i += 1
            
        return res
        
sol = Solution()
print(sol.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
print(sol.findReplaceString("abcd", [0, 2], ["ab","ec"], ["eee","ffff"]))
print(sol.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))
print(sol.findReplaceString("jjievdtjfb", [4,6,1], ["md","tjgb","jf"], ["foe","oov","e"]))