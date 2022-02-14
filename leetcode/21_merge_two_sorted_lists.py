from ListNode import ListNode
ListNode = ListNode()


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val < l2.val:
            head, headPointer, l1 = l1, l1, l1.next
        else:
            head, headPointer, l2 = l2, l2, l2.next

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next

        if l1 is None and l2 is not None:
            head.next = l2
        if l2 is None and l1 is not None:
            head.next = l1

        return headPointer


sol = Solution()
output = sol.mergeTwoLists(ListNode.to_ListNode(
    [1, 5]), ListNode.to_ListNode([2, 4]))
print(output)
