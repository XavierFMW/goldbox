import math


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

    def pop_child(self, node):
        if node is self.left:
            self.left = None
        elif node is self.right:
            self.right = None

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

    def index(self, index):
        try:
            return self.__get_node_at_index(index)
        except AttributeError:
            return None

    def insert(self, value, index):
        if self.root:
            parent = self.index((index - 1) // 2)
            parent.set_child(value, is_left=bool(index % 2))

        else:
            self.root = BinaryNode(value)

    def pop(self, index):
        removed = self.index(index)
        if removed == self.root:
            del self.root
            self.root = None
        else:
            removed.parent.pop_child(removed)

    def __get_node_at_index(self, index):
        current = self.root
        if index > 0:
            n = index + 1
            power = 2 ** math.floor(math.log(n, 2))
            base = power // 2
            total = n - power
            while base > 0:
                quotient = total // base
                current = current.right if quotient else current.left
                total -= quotient * base
                base //= 2
        return current
