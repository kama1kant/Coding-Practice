from typing import List
from ListNode import ListNode
ListNode = ListNode()


class Solution:
   def oddEvenList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None or head.next.next == None):
            return head
        odd_ptr = odd_head = head
        even_ptr = even_head = head.next
        head = head.next.next
        
        counter = 1
        while head:
            if counter%2 != 0:    
                odd_ptr.next = head
                odd_ptr = odd_ptr.next if odd_ptr.next != None else odd_ptr
            else:
                even_ptr.next = head
                even_ptr = even_ptr.next if even_ptr.next != None else even_ptr
    
            head = head.next
            counter += 1
        
        odd_ptr.next = even_head
        even_ptr.next = None
        
        return odd_head
        
sol = Solution()
output = sol.oddEvenList(ListNode.to_ListNode([]))
print(output)