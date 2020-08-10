#Creating the node

#Class for creating the nodes
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

#Class which create the tree
class Tree:
    def __init__(self):
        self.root = None
    # Function for inserting the data in tree
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        temp = self.root
        parent = None

        #Creating The nodes
        while temp != None:
            parent = temp
            if temp.data < data:
                temp = temp.right
            elif temp.data > data:
                temp = temp.left

        #Fedding the data into child of node
        if parent.data < data:
            parent.right = Node(data)
        else:
            parent.left = Node(data)
        return self.root
    #Print thr tree data in inOrder
    def inOrder(root):
        if root == None:
            return
        else:
            Tree.inOrder(root.left)
            print(root.data,end=" ")
            Tree.inOrder(root.right)
    ##Print thr tree data in preOrder        
    def preOrder(root):
        if root == None:
            return
        else:
            print(root.data,end=" ")
            Tree.preOrder(root.left)
            Tree.preOrder(root.right)
    #Print thr tree data in postOrder
    def postOrder(root):
        if root == None:
            return
        else:
            Tree.postOrder(root.left)
            Tree.postOrder(root.right)
            print(root.data,end=" ")           

if __name__ == "__main__":
    tree = Tree()
    for data in [7,5,1,8,3,6,0,9,4,2]:
        tree.insert(data)
    
    print("\ninOrder Traverser")
    Tree.inOrder(tree.root)
    print("\npreOrder Traverser")
    Tree.preOrder(tree.root)
    print("\npostOrder Traverser")
    Tree.postOrder(tree.root)

