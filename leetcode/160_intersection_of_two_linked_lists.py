from typing import List
from ListNode import ListNode
ListNode = ListNode()


class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLength(head):
            length = 0
            while(head):
                head = head.next
                length += 1
            return length
        
        len_a = getLength(headA)
        len_b = getLength(headB)
        if len_b > len_a:
            headA, headB = headB, headA
            len_a, len_b = len_b, len_a
        
        counter = len_a-len_b
        while(counter > 0):
            headA = headA.next
            counter -= 1
        
        while(headA):
            if(headA == headB):
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
        
sol = Solution()
output = sol.getIntersectionNode(ListNode.to_ListNode(
    [4, 1, 8, 4, 5]), ListNode.to_ListNode([5, 6, 1, 8, 4, 5]))
print(output)