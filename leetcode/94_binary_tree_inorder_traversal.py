from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def inorderTraversal(self, root) -> List[int]:
        ans = []

        def traversal(root):
            if(root == None):
                return
            traversal(root.left)
            ans.append(root.val)
            traversal(root.right)
            
        root = deserialize(root)
        traversal(root)
        return ans


sol = Solution()
output = sol.inorderTraversal('[]')
print(output)
