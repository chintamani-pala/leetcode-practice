"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                nextNode = curr.next
                if nextNode:
                    nextNode.prev = None
                # curr.next = None
                nextChild = curr.child
                curr.next = nextChild
                curr.child = None
                nextChild.prev = curr
                curr = curr.next
                newHead = self.flatten(curr)
                temp = newHead
                while temp.next is not None:
                    temp = temp.next
                temp.next = nextNode
                if nextNode:
                    nextNode.prev = temp
                curr = nextNode
            else:
                curr = curr.next

        return head

