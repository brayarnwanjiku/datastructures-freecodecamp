"""A linked List is a datastructure used for storing a sequence of elements 
Its data with some structure -- the sequence -- The order of the data needs to be maintained
These data items are connected to each other through links 
The Linked List that we aim at creating should have the following capabilities: 
Create a list with a given number of elements, Display the elements in the list, Find the number of elements in the list, 
More importantly: Retrieve the element at a given position in a list and Add or Remove elements in the list"""
#Let us create a class(blueprint for creating objects) for each individual Node in the List 
class Node(): 
    #lets give each node object the ability to store a value -- we do this by introducing the use of constructors 
    def __init__(self, a_number): 
        self.data = a_number
        self.next = None
        """Python works by first creating an object and stores the reference in temporary variable called self 
        Then, python calls the methon __init__(with self as the argument) which assigns self(temporary variable) with the value of the property"""
#Creating node objects 

node_one = Node(2)
node_two = Node(3)
node_three = Node(4)

#Create our Linked List class 
class LinkedList(): 
    def __init__(self): 
        self.head = None

#Assigning our node_one to the head property of our LinkedList 
list1 = LinkedList()
list1.head = node_one
#Assign the first node next property to the next node in line -- node_two
list1.head.next = node_two
# Assign the second node next property to the next node in line -- node_three 
list1.head.next.next = node_three

#Print the contents of the list
print(list1.head.data, list1.head.next.data, list1.head.next.next.data)#This is the entirerity of the list 
"""The structure of the Linked List is as follows: 
        head of the list: 2(first item ) 
        head.next = 3  (second item)
        head.next.next = 4 (third item)"""
#We can then print the actual memory locations of the list 
print(list1.head, list1.head.next, list1.head.next.next)

"""While the above implementation is great, we can improve it by adding a couple of arguments"""
class LinkedList1(): 
    def __init__(self): 
        self.head = None #initialize any list as empty i.e The head has no value 
    def append(self, value): # define an append function
        if self.head == None: #if the list is empty  
            self.head = Node(value) #initialize the list with the given value
        else: #if the list already has some elements 
            current_node = self.head #This variable will help traverse the list 
            while current_node.next is not None: # traverses the list up to the last node 
                current_node = current_node.next
            current_node.next = Node(value)

#adding the previously created node objects to this implementation 
list2 = LinkedList1()
list2.append(1)
list2.append(2)
list2.append(3)

print(list2.head.data, list2.head.next.data, list2.head.next.next.data, "This is the result ")

