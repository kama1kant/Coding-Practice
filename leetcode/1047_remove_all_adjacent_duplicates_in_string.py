class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) <= 0:
            return s

        stack = []
        for c in s:
            if len(stack) > 0 and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
