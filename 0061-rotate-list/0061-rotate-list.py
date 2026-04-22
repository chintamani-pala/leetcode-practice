# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        if not head or not head.next:
            return head
        # if nc>=k:
        #     return head
        newHead = self.reverse(head.next)
        first = head.next
        first.next = head
        head.next = None
        return newHead 
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        count = 0
        curr = head
        if not head or not head.next or not k:
            return head
        while curr:
            count += 1
            curr = curr.next
        if  k % count == 0:
            return head
        k = k%count
        curr = head
        for i in range(count-k-1):
            curr = curr.next
        nextNode = curr.next
        curr.next = None
        head1 = self.reverse(head)
        head2 = self.reverse(nextNode)
        head = head1
        while head1.next:
            head1 = head1.next
        head1.next = head2
        return self.reverse(head)

        