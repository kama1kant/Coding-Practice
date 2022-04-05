class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(node, low, up):
            if node is None:
                return True

            return low < node.val < up and traverse(node.left, low, node.val) and traverse(node.right, node.val, up)

        return traverse(root, float(-inf), float(inf))