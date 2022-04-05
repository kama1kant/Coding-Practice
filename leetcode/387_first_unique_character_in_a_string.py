class Solution:
    def firstUniqChar(self, s: str) -> int:
        mem = {}
        for i in range(26):
            mem[i] = 0

        for c in s:
            mem[ord(c)-ord('a')] += 1

        for i, c in enumerate(s):
            if mem[ord(c)-ord('a')] == 1:
                return i
        return -1