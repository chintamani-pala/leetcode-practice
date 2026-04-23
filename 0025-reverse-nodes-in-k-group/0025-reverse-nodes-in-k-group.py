# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        if head is None or head.next is None:
            return head
        newHead = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def findKthNode(self, head, k):
        temp = head
        k-=1
        while k>0 and temp:
            temp = temp.next
            k-=1
        return temp
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        count = 0
        if k ==1:
            return head
        
        while temp:
            count += 1
            temp = temp.next
            
        if k%count == 0:
            return self.reverseLL(head)
        kgroups = count//k
        curr = head
        count = 0
        while kgroups>0:
            kthNode = self.findKthNode(curr, k)
            print(kthNode)
            if kthNode is None:
                break
            print(kthNode.val)
            kthNextNode = kthNode.next
            kthNode.next = None
            #reverse the ll
            newHeadReverse = self.reverseLL(curr)
            
            if count == 0:
                head = newHeadReverse
                curr.next = kthNextNode
            else:
                prev.next = newHeadReverse
                curr.next = kthNextNode
            prev = curr
            curr = curr.next
            kgroups -= 1
            count += 1
        return head
        



