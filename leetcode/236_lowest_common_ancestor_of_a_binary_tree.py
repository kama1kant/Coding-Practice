from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ans = None
        def traversal(root):
            nonlocal ans
            nonlocal p
            nonlocal q
            cur = 0
            
            if not root:
                return 0
            if root.val == p.val or root.val == q.val:
                cur =  1
                
            left = traversal(root.left)
            right = traversal(root.right)

            if left + right + cur >= 2:
                ans = root
            
            return 1 if left or right or cur else 0
            
        
        root = deserialize(root)
        p = deserialize(p)
        q = deserialize(q)

        traversal(root)
        return ans.val


sol = Solution()
output = sol.lowestCommonAncestor('[3,5,1,6,2,0,8,null,null,7,4]', '[5]', '[1]')
print(output)
