"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        obj = {}
        while temp:
            newNode = Node(temp.val)
            obj[temp] = newNode
            temp = temp.next
        temp = head
        while temp:
            if temp.next is not None:
                obj[temp].next = obj[temp.next]
            if temp.random is not None:
                obj[temp].random = obj[temp.random]
            temp = temp.next
        return obj.get(head) 