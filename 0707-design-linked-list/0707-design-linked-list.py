class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):



    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        count = 0
        current = self.head
        while count != index:
            current = current.next
            count += 1
        return current.val

        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:    
            newPointer = self.head
            while newPointer is not None and newPointer.next is not None:
                newPointer = newPointer.next
            newPointer.next = newNode
        self.size  += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        newNode = Node(val)

        count = 0
        current = self.head
        while count != index-1:
            current = current.next
            count += 1
        newNode.next = current.next
        current.next = newNode
        self.size += 1
        

        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            count = 0
            while count != index-1:
                current = current.next
                count += 1
            current.next = current.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)