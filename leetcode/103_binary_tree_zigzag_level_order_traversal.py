from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        ans = []
        
        def getHeight(root):
            if root == None:
                return 0
            else:
                left_height = getHeight(root.left)
                right_height = getHeight(root.right)
                return max(left_height, right_height)+1
        
        def printLevel(root, level, nodes, is_even):
            if root == None:
                return
            if level == 1:
                if root!= None:
                    nodes.append(root.val)
            else:
                first, last = root.left, root.right
                if is_even:
                    first, last = root.right, root.left
                printLevel(first, level-1, nodes, is_even)
                printLevel(last, level-1, nodes, is_even)
            return nodes
        
        root = deserialize(root)
        height = getHeight(root)
        for i in range(height):
            nodes = []
            is_even = True if (i+1)%2 == 0 else False
            nodes = printLevel(root, i+1, nodes, is_even)
            ans.append(nodes)
        
        return ans        


sol = Solution()
output = sol.zigzagLevelOrder('[1,2,null,3,null,4,null,5]')
print(output)