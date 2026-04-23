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
    def flattenLL(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        prev = None
        while curr:
            prev = curr
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
                child_tail, child_head = self.flattenLL(curr)
                
                # temp = newHead[0]
                # while temp.next is not None:
                #     temp = temp.next
                if child_tail:
                    child_tail.next = nextNode
                if nextNode:
                    nextNode.prev = child_tail
                if nextNode:
                    curr = nextNode
            else:
                curr = curr.next

        return prev, head
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.flattenLL(head)[1]

