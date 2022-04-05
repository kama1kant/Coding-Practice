class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            return node1.val == node2.val and traverse(node1.left, node2.right) and traverse(node1.right, node2.left)

        return traverse(root.left, root.right)