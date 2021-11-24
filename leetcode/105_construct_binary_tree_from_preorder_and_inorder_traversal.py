from typing import List
from TreeNode import deserialize, drawtree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        root_index = 0
        def getHashmap(arr):
            hashmap = {}
            for i in range(len(arr)):
                hashmap[arr[i]] = i
            return hashmap
            
        def getTree(left, right):
            nonlocal hashmap
            nonlocal root_index
            if left > right:
                return

            node = deserialize('['+"".join(str([preorder[root_index]]))+']')
            root_index += 1
            node.left = getTree(left, hashmap[node.val]-1)
            node.right = getTree(hashmap[node.val]+1, right)
            return node
        
        hashmap = getHashmap(inorder)
        root = getTree(0, len(inorder)-1)
        # drawtree(root)
        return root


sol = Solution()
output = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(output)
