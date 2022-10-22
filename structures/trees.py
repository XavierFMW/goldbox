import chains
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
        self.__nodes = []
        self.__iteration = 0

        if length:
            self.root = BinaryNode(values[0])
            self.size = 1
            for index in range(1, length):
                value = values[index]
                self.insert(value, index)

        else:
            self.root = None
            self.size = 0

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
        self.size += 1

    def pop(self, index):
        removed = self.index(index)
        if removed == self.root:
            del self.root
            self.root = None
        else:
            removed.parent.pop_child(removed)
        self.size -= 1

    def depth_first(self, func, args=(), get_value=True):
        self.__dfs(self.root, func, args, get_value)

    def breadth_first(self, func, args=(), get_value=True):
        queue = chains.Queue()
        queue.push(self.root)

        while queue.head is not None:
            node = queue.pull()
            if node.left is not None:
                queue.push(node.left)
            if node.right is not None:
                queue.push(node.right)
            func(node.value if get_value else node, *args)

    def values(self, breadth_first=True):
        arr = []
        if breadth_first:
            self.breadth_first(arr.append)
        else:
            self.depth_first(arr.append)
        return arr

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

    def __dfs(self, node, func, args, get_value):
        if node is None:
            return
        func(node.value if get_value else node, *args)
        self.__dfs(node.left, func, args, get_value)
        self.__dfs(node.right, func, args, get_value)

    def __iter__(self):
        nodes = []
        self.breadth_first(nodes.append, get_value=False)
        self.__nodes = nodes
        self.__iteration = 0
        return self

    def __next__(self):
        if self.__iteration >= self.size:
            raise StopIteration
        value = self.__nodes[self.__iteration]
        self.__iteration += 1
        return value
