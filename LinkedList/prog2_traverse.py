class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        ptr = self.head
        if not ptr:
            print("Linked List is empty.")
            return
        print("Linked list is ",end="")
        while ptr:
            print("-> %d"%(ptr.data),end=" ")
            ptr = ptr.next

L = LinkedList()
L.traverse()
L.head = Node(10)
L.head.next = Node(20)
L.head.next.next = Node(30)
L.traverse()