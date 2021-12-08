


class Node(): 
    def __init__(self, a_number): 
        self.data = a_number #contents of the node object 
        self.next = None #pointer to the next node 

class LinkedList(): 
    def __init__(self): 
        self.head = None #This is first node on the linked list #For an empty list, the pointer in to None
    #define a class function to add/append elements in the list 
    def append(self, value): 
        if self.head == None: #if the list is empty 
            self.head = Node(value)#take the given value and make it the head
        else: #if the node has elements 
            current_node = self.head #the current_node variable acts as the counter 
            while current_node.next is not None: #traverse the list up to the last Node i.e the pointer to this node points to none
                current_node = self.head.next
            current_node.next = Node(value)
linkedlist = LinkedList()

linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
print(linkedlist.head.data, linkedlist.head.next.data, linkedlist.head.next.next.data)

        
