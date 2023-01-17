# find min
# find max
# calculate sum
# in order traversal
# pre order traversal

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def join_child(self, data):
        if data == self.data:
            return # for existent node
        
        if data < self.data:
            if self.left:
                self.left.join_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.join_child(data)
            else:
                self.right = BinarySearchTreeNode(data)