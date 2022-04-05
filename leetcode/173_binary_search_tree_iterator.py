class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        node = self.stack.pop()
        self.push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return self.stack