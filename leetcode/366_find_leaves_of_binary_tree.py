from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def findLeaves(self, root):
        def dfs(root):
            nonlocal ans
            if root == None:
                return -1

            level = max(dfs(root.left), dfs(root.right)) + 1
            if level < len(ans):
                ans[level].append(root.val)
            else:
                ans.append([root.val])
            return level

        ans = [[]]
        dfs(root)
        return ans


sol = Solution()
print(sol.findLeaves(deserialize('[1,2,3,4,5]')))
print(sol.findLeaves(deserialize('[1]')))