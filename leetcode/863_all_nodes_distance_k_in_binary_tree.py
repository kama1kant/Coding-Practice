from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def distanceK(self, root, target, k):
        parent, t, ans, visited = None, None, [], []

        def traverse(root, parent):
            nonlocal target, t
            if root is None:
                return
            elif root.val == target:
                t = root
            root.parent = parent
            traverse(root.left, root)
            traverse(root.right, root)

        def getNodes(root, k):
            nonlocal ans, visited
            if root == None or k < 0 or root in visited:
                return
            elif k == 0:
                ans.append(root.val)
            else:
                visited.append(root)
                getNodes(root.parent, k-1)
                getNodes(root.left, k-1)
                getNodes(root.right, k-1)

        traverse(root, parent)
        getNodes(t, k)
        return ans


sol = Solution()
print(sol.distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), 5, 2))
