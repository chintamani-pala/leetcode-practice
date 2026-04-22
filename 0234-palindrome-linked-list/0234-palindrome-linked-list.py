# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        if not head or not head.next:
            return head

        newHead = self.reverse(head.next)
        front = head.next
        front.next = head
        head.next = None

        return newHead

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head:
            return False
        if head.next is None:
            return True

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
         
        slow = self.reverse(slow)

        while slow and head:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
