from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dict, ans = collections.defaultdict(list), []

        def dfs(root):
            if root == None:
                return 'None'
            v = str(root.val) + ' l (' + dfs(root.left) + \
                ') r (' + dfs(root.right) + ')'

            if v not in dict:
                dict[v].append(root)
            elif dict[v][-1] != -1:
                dict[v].append(-1)
                ans.append(root)

            return v

        dfs(root)
        return ans


sol = Solution()
print(sol.findDuplicateSubtrees(deserialize('[1,2,3,4,null,2,4,null,null,4]')))
print(sol.findDuplicateSubtrees(deserialize('[2,1,1]')))
