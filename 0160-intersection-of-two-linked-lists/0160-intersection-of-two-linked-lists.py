# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h1 = headA
        h2 = headB
        
        while h1 != h2:
            h1 = h1.next
            h2 = h2.next
            if h1 is None and h2 is None:
                return None
            if h1 is None:
                h1 = headB
            if h2 is None:
                h2 = headA
            
        return h1
        