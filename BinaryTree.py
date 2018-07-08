class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_node(self, n):
        if n.value < self.value:
            if self.left is None:
                self.left = n
            else:
                self.left.add_node(n)

        elif n.value > self.value:
            if self.right is None:
                self.right = n
            else:
                self.right.add_node(n)

    def visit_node(self):
        if self.left is not None:
            self.left.visit_node()

        print(self.value)

        if self.right is not None:
            self.right.visit_node()

    def check_node(self, num):
        if self.value == num:
            print(f"Found {num}")
        elif num < self.value and self.left is not None:
            self.left.check_node(num)
        
        elif num > self.value and self.right is not None:
            self.right.check_node(num)
            

class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_to_root(self, new_value):
        if self.root is None:
            self.root = new_value
        else:
            self.root.add_node(new_value)
    
    def traverse(self):
        self.root.visit_node()

    def search(self, num):
        self.root.check_node(num)
