class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_start(self, data):

        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_specified(self, prev_node, data):
        
        if prev_node is None:
            print("previous node cannot be null")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
   
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return
    
    def remove_start(self):
        if self.head==None:
            return
        
        elif(self.head.next==None):
            self.head=None
        
        else:
            temp=self.head
            temp=temp.next
            temp.prev=None
            self.head=temp
    
    def remove_end(self):
        
        if self.head==None:
            return
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
               
    def remove_specified(self, ele):
        temp=self.head
        while(temp.data!=ele):
            temp=temp.next
        if temp.next==None:
            return
        elif temp.next.next==None:
            temp.next=None
        else:
            temp=temp.next
            temp.next=temp
            temp.prev=temp

    def show(self, node):

        while node:
            print(node.data, end="->")
            last = node
            node = node.next

if __name__=="__main__":
    dll= DoublyLinkedList()
    dll.insert_start(1)
    dll.insert_start(4)
    dll.insert_specified(dll.head,3)
    dll.insert_end(5)
    dll.insert_end(6)
    dll.show(dll.head)
    print("\n")
    dll.remove_start()
    dll.remove_end()
    dll.remove_specified(1)
    dll.show(dll.head)
    print("\n")
