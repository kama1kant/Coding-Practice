class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    def to_ListNode(self, arr):
        if len(arr) < 1:
            return None

        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=self.to_ListNode(arr[1:]))
    
    def to_List(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr