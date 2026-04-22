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
        first = head.next
        first.next = head
        head.next = None
        return newHead
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr = head
        newHead = ListNode(-1)
        curr1 = newHead
        count = 0
        while curr:
            count += 1
            node1 = ListNode(curr.val)
            curr1.next = node1
            curr = curr.next
            curr1 = curr1.next
        newHead = self.reverse(newHead.next)
        newlist = []
        curr = head
        for i in range((count//2)+1):
            newlist.append(curr.val)
            newlist.append(newHead.val)
            curr = curr.next
            newHead = newHead.next
        newlist = newlist[:count]
        curr = head
        while curr:
            curr.val = newlist.pop(0)
            curr = curr.next
        return head
        


        