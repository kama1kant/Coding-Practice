class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = head

        def recursive(node=head):
            nonlocal start
            if not node:
                return True
            elif recursive(node.next) and start.val == node.val:
                start = start.next
                return True
            else:
                return False

        return recursive()
