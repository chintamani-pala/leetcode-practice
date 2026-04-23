# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        if h1 is None and h2 is not None:
            return h2
        if h2 is None and h1 is not None:
            return h1
        if h1 is None and h2 is None:
            return h1
        if h1.val < h2.val:
            head = h1
            h1 = h1.next
        else:
            head = h2
            h2 = h2.next
        curr = head

        while h1 is not None and h2 is not None:
            if h1.val<h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        if h1 is None:
            curr.next = h2
        if h2 is None:
            curr.next = h1
        return head