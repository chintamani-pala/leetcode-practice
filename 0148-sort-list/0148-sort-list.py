# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        ##time complexity O(n^2)
        #space complexity O(1)
        # count = 1
        # curr = head
        # while curr.next is not None:
        #     curr = curr.next
        #     count += 1
        # while count>0:
        #     first = head
        #     second = head.next
        #     while second:
        #         if first.val>second.val:
        #             first.val, second.val = second.val, first.val
        #         first = first.next
        #         second = second.next
        #     count-=1
        # return head

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        curr = head
        index = 0
        while curr:
            curr.val = arr[index]
            index+=1
            curr = curr.next
        return head


