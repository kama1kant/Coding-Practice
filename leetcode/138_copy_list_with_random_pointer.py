class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        ptr = head
        while ptr != None:
            node = Node(ptr.val)
            node.next = ptr.next
            node.random = None
            ptr.next = node
            ptr = node.next

        ptr, new_ptr, new_head = head, head.next, head.next
        while ptr != None:
            if ptr.random != None:
                new_ptr.random = ptr.random.next

            ptr = ptr.next.next
            if ptr != None:
                new_ptr.next = new_ptr.next.next
                new_ptr = ptr.next

        return new_head