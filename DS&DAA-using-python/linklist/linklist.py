#Creating Node Class
class Node:
    #init method for creating the node 
    def __init__(self,data):
        self.data = data                #Assigning the data
        self.next = None                #Next data as none

class Linklist:
    def __init__(self):
        self.head = None                #Initializing Head of the link-list
    
    #insertion of the node at the end
    def insert_at_end(self,data):
        
        nn = Node(data)                 #Creating one node with data ans next id none
        if self.head == None:
            self.head = nn              #if head in none then head point to the nn
        else:
            temp = self.head
            while temp.next != None:    #find the last position to insert the node
                temp = temp.next
            temp.next = nn              #if temp.next is none that mines the next haa no node add then set the temp.next to nn
            
    #insertion of the node at beginning
    def insert_at_beg(self,data):

        nn = Node(data)                 #Creating one node with data ans next id none
        if self.head == None:
            self.head = nn              #if head in none then head point to the nn
        else:
            temp = self.head
            self.head = nn
            nn.next = temp
            
    #insertion of the node at before the given node
    def insert_pre_node(self,pre_node_data,val):
        nn = Node(val)
        if self.head == None:
            self.head = nn
        else:
            temp = self.head
            while temp.next.data != pre_node_data:
                temp = temp.next

            nn.next = temp.next
            temp.next = nn
            
    #insertion of the node at after the given node
    def insert_aft_node(self,aft_node_data,val):
        nn = Node(ValueError)
        if self.head == None:
            self.head = nn
        else:
            temp = self.head
            while temp.data != aft_node_data:
                temp = temp.next

            nn.next = temp.next
            temp.next = nn

    #Function to print all the node data from linklist        
    def traverse(self):
        if self.head == None:
            return "Link list is empty"

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    #Function to delete the element from the link list
    def delete_element(self,val):
        if self.head == None:
            return "Link list is empty"

        temp = self.head
        next_temp = temp.next

        if temp.data == val:
            self.head = next_temp
        else:
            while next_temp.data != val:
                temp = temp.next
                next_temp = next_temp.next
            temp.next = next_temp.next

#Driving the code
if __name__ == "__main__":
    llist = Linklist()

    """
    #Creating the Three Node having one is head
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #Assigning node.next to other node
    llist.head.next = second #link the head to second node
    second.next = third      #link the second to third node
    third.next = None        #link the third to None node


    #Printing the add
    print(type(llist.head))
    print(type(second),second)
    print(type(third),third) 

    #Printing the data od the each node
    print("-------------------")
    print(llist.head.next)
    print(second.next)
    print(third.next)

    print("-------------------")
    print(llist.head.data)
    print(second.data)
    print(third.data)
    """
    x = [1,2,3,4,5]
    for i in x:
        llist.insert_at_end(i)
        #llist.insert_at_beg(i)

    #llist.insert_pre_node(6,5)
    #llist.insert_aft_node(6,5)
    
    llist.delete_element(1)

    llist.traverse()