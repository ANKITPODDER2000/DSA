class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_beg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def insert_end(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        node.next = ptr.next
        ptr.next = node
        
    def insert_anywhere(self):
        val = int(input("Enter the value after which you want to insert : "))
        if not self.head:
            print("Linked List is empty.Insertion not possible")
        ptr = self.head
        while ptr:
            if ptr.data == val:
                ins = int(input("Enter value to insert : "))
                node = Node(ins)
                node.next = ptr.next
                ptr.next = node
            ptr = ptr.next
    
    def traverse(self):
        ptr = self.head
        if not ptr:
            print("Linked List is empty.")
            return
        print("Linked list is ",end="")
        while ptr:
            print("-> %d"%(ptr.data),end=" ")
            ptr = ptr.next
        print(" -> None")
        
    