from typing import List
from ListNode import ListNode
ListNode = ListNode()

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:        
        length = 0
        prev = cur = head
        
        while head:
            length += 1
            head = head.next
        
        if(length == 0):
            return head
        
        head = cur
        k = k%length
        if(k == 0):
            return head
        
        while k > 0:
            cur = cur.next
            k -= 1
            
        while cur.next:
            cur = cur.next
            prev = prev.next
        
        new_head = prev.next
        prev.next = None
        cur.next = head
        
        return new_head
        
        
sol = Solution()
ans = sol.rotateRight(ListNode.to_ListNode([]), 0)
print(ans)