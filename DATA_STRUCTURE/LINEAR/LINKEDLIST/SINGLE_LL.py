class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    
    def insert_start(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node


    def insert_specified(self, prev_node, new_data):

        if prev_node is None:
            print("Node not found...")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

  
    def insert_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
    
    def remove_start(self,head):
        
        if self.head is None:
            return
        else:
            self.head=head.next
        
    def remove_end(self,head):
        temp=head
        if self.head is None:
            return
        else:
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            
    def remove_specified(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

       
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

       
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next


    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

  
    def sortll(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
            
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    
    def show(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end=" ")
            temp = temp.next
        print("\n",end=" ")
        print("\n",end=" ")

if __name__ == '__main__':

    l = LinkedList()
    
    #-----------insertion--------
    
    l.insert_start(1)
    l.insert_end(2)
    l.insert_start(3)
    l.insert_specified(l.head.next,4)
    l.show()
    
    #---------searching-------
    
    if l.search(4)==True:
        print("Found")
        print("\n",end=" ")
    else:
        print("Notfound")
        print("\n",end=" ")
        
    #---------sorting---------
    
    l.sortll(l.head)
    l.show()
    
    #--------deletion---------
    
    l.remove_start(l.head)
    l.show()
    l.remove_end(l.head)
    l.show()
    l.remove_specified(2)
    l.show()
