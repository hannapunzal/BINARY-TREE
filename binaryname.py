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
        
    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            max_val = self.max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    full_name = ["H","A","N","N","A","F","A","I","T","H","P","U","N","Z","A","L",]
    full_name_tree = build_tree(full_name)
    # display
    print("--> Full name: ",full_name)
    print()
    #traverse
    print("--> In order traversal: ",full_name_tree.in_order_traversal())
    print("--> Pre order traversal: ",full_name_tree.pre_order_traversal())
    print("--> Post order traversal: ",full_name_tree.post_order_traversal())
    #min and max
    print()
    print("--> Min: ",full_name_tree.min())
    print("--> Max: ",full_name_tree.max())
    print()
    #delete
    full_name_tree.delete("A")
    print("--> Removed letter A: ",full_name_tree.in_order_traversal())
    print()
    #search
    print("Is there an E in the given name? ",full_name_tree.search("E"))
    print("Is there a P in the given name? ", full_name_tree.search("P"))