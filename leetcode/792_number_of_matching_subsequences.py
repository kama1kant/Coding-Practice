from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hashmap, ans = collections.defaultdict(list), 0
        for i, c in enumerate(s):
            hashmap[c].append(i)

        for w in words:
            i, exists = -1, True
            for c in w:
                j = bisect.bisect_left(hashmap[c], i)
                if j >= len(hashmap[c]) or hashmap[c][j] < i:
                    exists = False
                    break
                i = hashmap[c][j] + 1
            if exists:
                ans += 1

        return ans


sol = Solution()
print(sol.numMatchingSubseq("aabcde", ["bb", "acd", "ace"]))
print(sol.numMatchingSubseq("dsahjpjauf", [
      "ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
print(sol.numMatchingSubseq("aabcde", ["bb","acd","ace"]))
