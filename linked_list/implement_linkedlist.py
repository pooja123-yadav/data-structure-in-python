class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
             self.head = new_node
             return
        current_node = self.head
        while current_node.next:
             current_node = current_node.next

        current_node.next = new_node


    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == position:
            return self.insertAtBegin(data)
        else:
            while current_node.next != None and position+1 != index:
                position += 1
                current_node = current_node.next

            if current_node.next != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else: 
                print("Index is not present")

    def updateNode(self,val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val

        while (current_node != None and position != index):
            position += 1
            current_node = current_node.next

        if current_node != None:
            current_node.data = val
        else:
            print("Index is not found to update node data")
    
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None
 
    def remove_at_index(self, index):
        if self.head is None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node != None and position+1 != index:
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not found to remove node")


    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return
        else:
            while current_node != None and current_node.next.data != data:
                current_node = current_node.next
            
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                return
    

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        return size

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print()

llist = LinkedList()

# add nodes to the linked list
llist.insertAtBegin('a')
llist.insertAtEnd('g')
llist.insertAtEnd('d')

# add nodes to the end of linked list 
llist.insertAtEnd('e')

# add nodes to the index of linked list
llist.insertAtIndex('c',2)

# print the linked list
print("Node Data")
llist.printLL()

# print size of the linked list
print(f"Linkedlist Size: {llist.sizeOfLL()}")

# update linked list value of some index
print("update linkedlist value of a node")
llist.updateNode('b', 1)

# # print the linked list
print("Node Data")
llist.printLL()

# remove a node
llist.remove_node('d')

print("New Node Data")
llist.printLL()