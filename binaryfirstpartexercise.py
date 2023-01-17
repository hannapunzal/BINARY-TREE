# find min
# find max
# calculate sum
# in order traversal
# post order traversal
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

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
        
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def obtain_max(self):
        if self.right is None:
            return self.data
        return self.right.obtain_max()
    
    def obtain_min(self):
        if self.left is None:
            return self.data
        return self.left.obtain_min()

    def sum(self):
        if self.left:
            sum_left = self.left.sum()
        else:
            sum_left = 0
        if self.right:
            sum_right = self.right.sum()
        else:
            sum_right = 0
        return self.data + sum_left + sum_right

    def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range(1,len(elements)):
            root.join_child(elements[1])
        
        return root
        

