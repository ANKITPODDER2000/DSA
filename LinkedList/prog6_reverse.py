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
            
    def delete(self,val):
        if not self.head:
            return
        if self.head.data == val:
            ptr = self.head
            ptr = ptr
            del(ptr)
            self.head = self.head.next
            self.delete(val)
        else:
            ptr1 = self.head
            ptr2 = self.head.next
            while ptr2:
                if ptr2.data == val:
                    ptr1.next = ptr2.next
                    del(ptr2)
                    ptr2 = ptr1.next
                else:
                    ptr1 = ptr2
                    ptr2 = ptr2.next
                    
    def reverse(self):
        prev = None
        nxt  = None
        if not self.head:
            print("Linked List is empty.")
            return 
        ptr = self.head
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        self.head = prev
        
    
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
        
    