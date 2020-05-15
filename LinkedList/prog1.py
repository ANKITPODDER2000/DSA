class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __inint___(self):
        self.head = None

L = LinkedList()
L.head = Node(10)
L.head.next = Node(20)
L.head.next.next = Node(30)