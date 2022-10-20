
class BinaryNode:

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left, self.right = left, right
        self.parent = parent

    def set_child(self, value, is_left=True):
        node = BinaryNode(value, parent=self)
        if is_left:
            self.left = node
        else:
            self.right = node

    def display_value(self):
        return f'"{self.value}"' if isinstance(self.value, str) else str(self.value)

    def __str__(self):
        return f"BinaryNode({self.display_value()})"


class BinaryTree:

    def __init__(self, values=()):
        length = len(values)

        if length:
            self.root = BinaryNode(values[0])
            for index in range(1, length):
                value = values[index]
                self.insert(value, index)

        else:
            self.root = None

    def insert(self, value, index):
        parent = self.root
        if parent:
            n = index + 1
            while n > 2:
                mod = n % 2
                if mod:
                    parent = parent.right
                else:
                    parent = parent.left
                print(parent)
                n //= 2
            parent.set_child(value, bool(n % 2))

        else:
            self.root = BinaryNode(value)

