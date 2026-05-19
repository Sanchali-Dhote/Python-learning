# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None


# linkedlist = Linkedlist()

# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #connecting nodes
# linkedlist.head.next = second
# second.next = third
# third.next  = fourth

# #display linkedlist
# while linkedlist.head.next != None:
#     print(linkedlist.head.data,"|",linkedlist.head.next,"->",end=" ")
#     linkedlist.head.next = linkedlist.head.next
#===========================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,value):
        self.node=Node(value)

        if self.head is None:
            self.head=self.node
            self.tail=self.node

        else:
            self.tail.next=self.node
            self.tail=self.node

    def display(self):

        temp=self.head

        while temp is not None:
            print(temp.data,'|','->',end='')

            temp=temp.next

        print()

if __name__ == '__main__':

    object = Linkedlist()

    # menu driven options
    while True:

        print('1.Add Node LinkedList:')
        print('2.Add Node in Beginning:')
        print('3.Add Node in Between:')
        print('4.Add Node in End:')
        print('5.Display Linked List:')
        print('6.Exit')

        ch=int(input('Enter your choice:'))

        # Add Node
        if ch==1:

            value=int(input('Enter value for node:'))

            object.addNode(value)

            print('Node added successfully in single Linkedlist:')

        # Add in Beginning
        elif ch==2:

            value=int(input('Enter value for node:'))

            newnode=Node(value)

            newnode.next=object.head

            object.head=newnode

            print('Node added at beginning successfully')

        # Add in Between
        elif ch==3:

            position=int(input('Enter position:'))

            value=int(input('Enter value for node:'))

            newnode=Node(value)

            temp=object.head

            for i in range(position-1):

                temp=temp.next

            newnode.next=temp.next

            temp.next=newnode

            print('Node added in between successfully')

        # Add in End
        elif ch==4:

            value=int(input('Enter value for node:'))

            newnode=Node(value)

            object.tail.next=newnode

            object.tail=newnode

            print('Node added at end successfully')

        # Display
        elif ch==5:

            object.display()

        # Exit
        elif ch==6:

            print('Program Ended')

            break
