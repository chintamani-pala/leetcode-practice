# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        count = 0
        curr = head
        if head.next is None:
            return None
        while curr:
            count += 1
            curr = curr.next
        if count%2==0:
            fast = head.next
        else:
            fast = head.next.next
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if slow and slow.next:
            slow.next = slow.next.next
        return head