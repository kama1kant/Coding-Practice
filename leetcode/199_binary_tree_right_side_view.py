class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(root, i):
            nonlocal ans
            if root == None:
                return root
            if i > len(ans) - 1:
                ans.append(root.val)

            traverse(root.right, i+1)
            traverse(root.left, i+1)

        traverse(root, 0)
        return ans
