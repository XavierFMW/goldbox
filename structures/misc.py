import operator
import trees
import copy


### RangeDict ###

class RangeDict:
    ADD_INPUT_ERROR = TypeError("RangeDict addition operand must be of type 'Tuple.'")

    def __init__(self, round_up_keys=True):
        self.dictionary = {None: None}
        self.keys = trees.BinarySearchTree()
        self.round_up = round_up_keys

    def add(self, key, value):
        self.dictionary[key] = value
        self.keys.push(key)

    def remove(self, key):
        self.dictionary.pop(key)
        self.keys.pull(key)

    def get(self, key):
        if key in self.keys:
            true_key = key
        else:
            true_key = self.keys.get_nearest_value(key, self.round_up)

        return self.dictionary[true_key]

    def copy(self):
        return copy.deepcopy(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.dictionary == other.dictionary
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iadd__(self, other):
        if isinstance(other, tuple) and len(other) >= 2:
            self.add(other[0], other[1])
            return self
        else:
            raise self.ADD_INPUT_ERROR

    def __add__(self, other):
        c = self.copy()
        c += other
        return c

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        output = "RangeDict{"
        for key, value in self.dictionary.items():
            if key is not None:
                output += f"{key}: {value}, "
        output += "}"

        return output


### ArithmeticTree ###

class ValueNode:

    DIGITS = "0123456789."
    INVALID_DIGIT_ERROR = TypeError("Invalid digit passed to ValueNode.")

    def __init__(self, number):
        self.number = str(number)

    def add_digit(self, digit):
        if isinstance(digit, str) and digit in self.DIGITS:
            self.number += digit
        else:
            raise self.INVALID_DIGIT_ERROR

    def solve(self):
        return float(self.number)


class OperationNode:

    # Sign: (operation, precedence)
    # Operations with a lower precedence are executed first.
    # Operations with equal precedence are executed left to right.
    OPERATIONS = {
        "+": (operator.add, 0),
        "-": (operator.sub, 0),
        "*": (operator.mul, 1),
        "/": (operator.truediv, 1),
    }

    SIGNS = OPERATIONS.keys()
    INVALID_SIGN_ERROR = TypeError("Invalid sign passed to OperationNode.")

    def __init__(self, sign):
        self.left = None
        self.right = None
        if sign in self.SIGNS:
            self.operation, self.precedence = self.OPERATIONS[sign]
        else:
            self.operation, self.precedence = None, None
            raise self.INVALID_SIGN_ERROR

    def add_operand(self, node):
        if self.left is None:
            self.left = node
        else:
            self.right = node

    def solve(self):
        left_value = self.left.solve()
        right_value = self.right.solve()
        return self.operation(left_value, right_value)


class ArithmeticTree:

    def __init__(self, string=None):
        self.root = None
        self.last = None
        if string:
            for char in string:
                self.push(char)

    def push(self, char, rank=0):
        node = self._get_node_from_char(char, rank)
        if self.root is None:
            self.root, self.last = node, node
        else:
            self.last.add_operand(node)

    def solve(self):
        value = self.root.solve
        self._truncate(value)
        return value

    @staticmethod
    def _get_node_from_char(char, rank=0):
        if char in OperationNode.SIGNS:
            node = OperationNode(char)
            node.precedence += rank
            return node
        else:
            return ValueNode(char)

    def _truncate(self, value):
        new = ValueNode(value)
        self.root, self.last = new, new
