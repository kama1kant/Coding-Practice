from typing import List
import math
from TreeNode import deserialize, drawtree


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        ans = math.inf
        def traversal(root):
            nonlocal k
            nonlocal ans
            if root == None or k < 0:
                return None
            traversal(root.left)
            if k == 1:
                print('ans ', root.val)    
                ans = root.val
            k -= 1
            traversal(root.right)
        
        traversal(deserialize(root))
        return ans

sol = Solution()
output = sol.kthSmallest('[5,3,6,2,4,null,null,1]', 3)
print(output)
