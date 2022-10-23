import chains
import math


class BinaryNode:

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left, self.right = left, right
        self.parent = parent
        self.children = (0 if left is None else 1) + (0 if right is None else 1)

    def set_child(self, value, is_left=True):
        node = BinaryNode(value, parent=self)
        if is_left:
            self.children += 1 if self.left is None else 0
            self.left = node
        else:
            self.children += 1 if self.right is None else 0
            self.right = node

    def pop_child(self, node):
        if node is not None:
            if node is self.left:
                self.left = None
                self.children -= 1
            elif node is self.right:
                self.right = None
                self.children -= 1

    def get_display_value(self):
        return f'"{self.value}"' if isinstance(self.value, str) else str(self.value)

    def __str__(self):
        return f"BinaryNode({self.get_display_value()})"


class BinaryTree:

    SEPARATOR = ", "
    PREFIX = "BinaryTree("
    SUFFIX = ")"

    def __init__(self, values=(), reverse=False):
        self.root = None
        self.size = 0
        self.__nodes = []
        self.__iteration = 0

        if values:
            self.extend(values, reverse)

    def extend(self, values, reverse=False):
        for index in range(len(values)):
            i = -(index + 1) if reverse else index
            self.insert(values[i], index)

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
        if removed is self.root:
            del self.root
            self.root = None
        else:
            removed.parent.pop_child(removed)
        self.size -= 1

    def values(self, breadth_first=True):
        arr = []
        if breadth_first:
            self.breadth_first(arr.append)
        else:
            self.depth_first(arr.append)
        return arr

    def depth_first(self, func, args=(), get_value=True):
        self.__dfs(self.root, func, args, get_value)

    def breadth_first(self, func, args=(), get_value=True):
        queue = chains.Queue()
        if self.root:
            queue.push(self.root)

        while queue.head is not None:
            node = queue.pull()
            if node.left is not None:
                queue.push(node.left)
            if node.right is not None:
                queue.push(node.right)
            func(node.value if get_value else node, *args)

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

    def __str__(self, separator=None, prefix=None, suffix=None):
        sep = self.SEPARATOR if separator is None else separator
        suf = self.SUFFIX if suffix is None else suffix
        output = self.PREFIX if prefix is None else prefix

        remaining = self.size
        for node in self:
            output += node.get_display_value()
            remaining -= 1
            output += "" if remaining == 0 else sep

        output += suf
        return output


class BinarySearchTree:

    def __init__(self, values=(), reverse=False):
        self.root = None
        self.size = 0
        self.__values = set()

        if values:
            self.extend(values, reverse)

    def extend(self, values, reverse=False):
        step = -1 if reverse else 1
        for value in values[::step]:
            self.push(value)

    def push(self, value):

        parent = self.__get_parent_of_value(value)
        if parent:
            parent.set_child(value, is_left=(value < parent.value))

        else:
            self.root = BinaryNode(value)
        self.size += 1
        self.__values.add(value)

    def pull(self, value):
        if value in self.__values:
            node = self.get_node_of_value(value)
            self.__delete_node(node)
            self.size -= 1
            self.__values.discard(value)
            return value

    def __get_parent_of_value(self, value):
        parent = None
        current = self.root
        while current:
            parent = current
            current = parent.right if value > parent.value else parent.left
        return parent

    def get_node_of_value(self, value):
        current = self.root
        while current and current.value != value:
            current = current.left if value < current.value else current.right
        return current

    def __delete_node(self, node):
        parent = node.parent

        if parent is None:
            self.__delete_root()
        elif node.children == 0:
            self.__delete_leaf_node(node, parent)
        elif node.children == 1:
            self.__delete_one_child_node(node, parent)
        else:
            self.__delete_two_child_node(node)

    def __delete_root(self):
        root = self.root

        if root.children == 0:
            self.root = None
        elif root.children == 1:
            child = root.right if root.left is None else root.left
            child.parent = None
            self.root = child
        else:
            replacement = self.__get_next_highest(root)
            self.root.value = replacement.value
            self.__delete_node(replacement)

    @staticmethod
    def __delete_leaf_node(node, parent):
        parent.pop_child(node)

    @staticmethod
    def __delete_one_child_node(node, parent):
        child = node.right if node.left is None else node.left
        child.parent = parent
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child

    def __delete_two_child_node(self, node):
        replacement = self.__get_next_highest(node) if node.value <= self.root.value \
            else self.__get_next_lowest(node)
        node.value = replacement.value
        self.__delete_node(replacement)

    @staticmethod
    def __get_next_highest(node):
        current = node.right
        while current.left:
            current = current.left
        return current

    @staticmethod
    def __get_next_lowest(node):
        current = node.left
        while current.right:
            current = current.right
        return current
