class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_end(self,data):
        ptr = self.head
        node = Node(data)
        if not ptr:
            self.head = node
            return
        while ptr.next:
            ptr = ptr.next
        ptr.next = node
    
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
L.insert_end(10)
L.insert_end(20)
L.insert_end(30)
L.traverse()