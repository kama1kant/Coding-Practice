from typing import List
from ListNode import ListNode
ListNode = ListNode()


class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        def getLength(l: ListNode):
            count = 0
            while l:
                count += 1
                l = l.next
            return count
       
        len1 = getLength(l1)
        len2 = getLength(l2)
        root = head = l1 if len1>len2 else l2
        
        while l1 or l2:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            
            head.val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            head = head.next if head.next != None else head
            
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        
        if carry > 0:
            head.next = ListNode.to_ListNode([carry])
        return root
        
        
sol = Solution()
output = sol.addTwoNumbers(ListNode.to_ListNode([2, 4, 3]), 
                           ListNode.to_ListNode([5, 6, 4]))
print(output)
