# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        if size == 1:
            head = head.next
            return head
        if size == n:
            if head is not None:
                head = head.next
            return head
        count = 0
        current = head
        while count < size-n-1:
            count += 1
            current = current.next
        current.next = current.next.next

        return head
        
        