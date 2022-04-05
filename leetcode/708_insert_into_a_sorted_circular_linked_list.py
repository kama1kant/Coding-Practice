class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal)
            node.next = node
            return node

        ptr = head
        while ptr.next != head:
            if ptr.val <= ptr.next.val:
                if ptr.val <= insertVal <= ptr.next.val:
                    break
            else:
                if insertVal <= ptr.next.val or insertVal >= ptr.val:
                    break

            ptr = ptr.next

        node = Node(insertVal, ptr.next)
        ptr.next = node

        return head
