class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        
        newNode = Node(data)

      
        self.last = newNode

      
        self.last.next = self.last
        return self.last

   
    def insert_start(self, data):

        
        if self.last == None:
            return self.addToEmpty(data)


        newNode = Node(data)

    
        newNode.next = self.last.next

     
        self.last.next = newNode

        return self.last

    def insert_end(self, data):

        if self.last == None:
            return self.addToEmpty(data)


        newNode = Node(data)

       
        newNode.next = self.last.next


        self.last.next = newNode

  
        self.last = newNode

        return self.last


    def insert_specified(self, data, item):

       
        if self.last == None:
            return None

        newNode = Node(data)
        p = self.last.next
        while p:

           
            if p.data == item:
                newNode.next = p.next
                p.next = newNode

                if p == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def remove_end(self,last):
        temp=self.last
        while temp.next is not self.last:
            temp=temp.next
        temp.next=self.last.next
        self.last=self.last.next
    
    def remove_start(self,last):
        temp=self.last
        while temp.next.next is not self.last:
            temp=temp.next
        temp.next=self.last
        
    def remove_specified(self, last, key):

        if last == None:
            return


        if (last).data == key and (last).next == last:

            last = None

        temp = last
        d = None
        if (last).data == key:

            while temp.next != last:
                temp = temp.next

            temp.next = (last).next
            last = temp.next
        while temp.next != last and temp.next.data != key:
            temp = temp.next

        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return last

    def show(self):
        if self.last == None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.last.next:
                break


# Driver Code
if __name__ == "__main__":

    cll = CircularLinkedList()
    
    #---insertion--------
    l=cll.addToEmpty(1)
    l=cll.insert_start(2)
    l=cll.insert_end(3)
    l=cll.insert_specified(4,1)
    cll.show()
    
    #----deletion----
    l=cll.remove_specified(l,4)
    print("\n")
    l=cll.remove_end(l)
    
    print("\n")
    cll.show()
    l=cll.remove_start(l)
    print("\n")
    cll.show()

    
