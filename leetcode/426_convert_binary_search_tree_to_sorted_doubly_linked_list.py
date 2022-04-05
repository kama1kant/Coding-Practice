class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def preorder(root):
            nonlocal head, prev
            if root == None:
                return root
            
            preorder(root.left)
            if head == None:
                head = prev = root
            else:
                root.left, prev.right, prev = prev, root, root
            preorder(root.right)
        
        head, prev = None, None
        if root == None:
            return root
        
        preorder(root)
        head.left, prev.right = prev, head
        return head
        
sol = Solution()
sol.treeToDoublyList([4,2,5,1,3])