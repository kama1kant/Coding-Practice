from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split('/')
        pathArr = ' '.join(pathArr).split()
        stack = []
        for ele in pathArr:
            if len(stack) > 0 and ele == '..':
                stack.pop()
            elif ele != '..' and ele != '.':
                stack.append(ele)

        ans = '/'.join(stack)
        return '/' + ans