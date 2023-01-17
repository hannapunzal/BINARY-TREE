# Use the letters in your fullname as the content of the binary tree

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return #existent node

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elemements = []
        if self.left:
            elemements += self.left.in_order_traversal()
        
        elemements.append(self.data)

        if self.right:
            elemements += self.right.in_order_traversal()
        
        return elemements