# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

LinkedList Insertion and Traversal
class Node:
    def __init__(self,data,next=None):
        self.data =data
        self.next = next
        class LinkedList:
    def __init__(self):
        self.head =None
            #Insertion at the end
    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next): #going till the end of list by next -> next -> next
                current = current.next
            current.next = newNode #adding the specified element at the end of the above list
        else:
            self.head = newNode
            #insertion after specifying the prev pointr
    def insertAfter(self,prev,data):
        '''
            here the prev denotes the node object by its next pntr reference
            TODO Implement a mechanism by which valuecan be nserted into a
            specific index without supplying the pntr reference
                        What's happening here?
            -> using to assign the value of next of prevNode as next of this new node
            and assigning the next of prevNode as actual value of newNode

        '''
        if prev is None:
            print("No node exists")
