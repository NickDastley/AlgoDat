class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.data
        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        yield self.data
        if self.left:
            yield from self.left.inorder()
        if self.right:
            yield from self.right.inorder()

    def print_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def postorder(self):
        if self.left:
            yield from self.left.postorder()
        if self.right:
            yield from self.right.postorder()
        yield self.data

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.data)


my_root = Node("F")
my_root.insert("B")
my_root.insert("A")
my_root.insert("D")
my_root.insert("C")
my_root.insert("E")
my_root.insert("G")
my_root.insert("I")
my_root.insert("H")

my_root.print()
print("---")
my_root.print_preorder()
print("---")
my_root.print_postorder()


def invert(root):
    if root:
        root.left, root.right = root.right, root.left
        if root.left:
            invert(root.left)
        if root.right:
            invert(root.right)

print("---")
invert(my_root)
my_root.print()