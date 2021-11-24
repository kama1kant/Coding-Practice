from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def connect(self, root):
        root = deserialize(root)
        
        def getHeight(root):
            if root == None:
                return 0
            l_height = getHeight(root.left)
            r_height = getHeight(root.right)
            return max(l_height, r_height)+1
        
        def level_order_traversal(root, level):
            nonlocal prev
            if level == 1:
                if prev == None:
                    prev = root
                else:
                    prev.next = root
                    prev = root
            else:
                level_order_traversal(root.left, level-1)
                level_order_traversal(root.right, level-1)
            return
        
        prev = None
        height = getHeight(root)
        for i in range(height):
            level_order_traversal(root, i+1)
            prev.next = None
            prev = None
        return root

sol = Solution()
output = sol.connect('[1,2,3,4,5,6,7]')
print(output)
