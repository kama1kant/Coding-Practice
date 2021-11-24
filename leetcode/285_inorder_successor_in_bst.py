from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def inorderSuccessor(self, root, p):
        found_node = False
        ans = None

        def traversal(root, p):
            nonlocal found_node
            nonlocal ans
            if root == None:
                return None
    
            traversal(root.left, p)
            print(root.val)
                   
            if root.val == p.val:
                found_node = True
            elif found_node:
                ans = root
                found_node = False
                return
        
            traversal(root.right, p)

        traversal(deserialize(root), deserialize(p))
        return ans.val
        
sol = Solution()
output = sol.inorderSuccessor('[5,3,6,2,4,null,null,1]', '[1]')
print(output)
