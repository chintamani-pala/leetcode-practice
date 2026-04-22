# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(-1)
        sum = 0
        carry = 0
        curr = head
        while l1 or l2 or carry>0:
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            if carry>0:
                sum+=carry
            newNode = ListNode(sum%10)
            carry = sum/10
            sum=0
            curr.next = newNode
            curr = curr.next
        return head.next