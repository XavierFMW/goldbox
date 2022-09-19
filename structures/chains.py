
class Node:

    def __init__(self, value, parent=None, child=None):

        self.value = value
        self.parent = parent
        self.child = child
    
    
    def display_value(self):
        return f'"{self.value}"' if isinstance(self.value, str) else self.value 


    def __str__(self):
        return f"Node({self.display_value()})"



class Chain:

	SEPARATOR = " > "

	def __init__(self, array=None):
        
		if array:
            
			current = None 
			for i, value in enumerate(array):    
                node = Node(value, current)

                if current:
                    current.child = node
                else:
                    self.head = node

                current = node
                self.tail = current
                
        else:
            self.head = None
            self.tail = None


    def __str__(self):
        
        if self.head:

            output = ""

            current = self.head
            while current:
                output += f"{current.display_value()}{self.SEPARATOR if current != self.tail else ''}"
                current = current.child

            return output

        else:
            return self.SEPARATOR 



class LinkedList(Chain):

    MISSING_VALUE_ERROR = ValueError("Value not contained within linked list.")
    MISSING_INDEX_ERROR = IndexError("Value at index does not exist within linked list.")

    def __init__(self, array=None):
        super().__init__(array)
        self.length = len(array)
        self.iteration = self.head
    

    def append(self, value):
        node = Node(value, self.tail)
        length += 1    

        if self.tail:
            self.tail.child = node

        else:
            self.head = node

		self.tail = node


    def prepend(self, value):
        node = Node(value, child=self.head)
        length += 1

        if self.head:
            self.head.parent = node

        else:
            self.tail = node

		self.head = node


    def insert(self, value, index):

        old = self.index(index)
        new = Node(value, child=old)

        if old == self.head:
            self.head = new

        else:
            old.parent.child = new
            new.parent = old.parent

        old.parent = new


    def extend(self, array, reverse=False, prepend=False):
        
        if prepend:
            reverse = not reverse  # Prepending each element will naturally reverse the order of the inserted list, requiring a subsequent reversal.
            executed = self.prepend
        else:
            executed = self.append

        if reverse:
            i = len(array) - 1
            while i >= 0:
                executed(array[i])
                i -= 1

        else:
            for value in array:
                executed(value)


    def remove(self, value):
        node = self.search(value)
        self.__remove_node(node)


    def pop(self, index=0):
        node = self.index(index)
        self.__remove_node(node)


    def search(self, value):

        for node in self:
            if node.value == value:
                return node
        
        raise self.MISSING_VALUE_ERROR


    def index(self, index):
        
        count = 0
        for node in self:
            if count == index:
                return node
            count += 1

        raise self.MISSING_INDEX_ERROR


    def values(self):
        for node in self:
            yield node.value


    def __remove_node(self, node):

        if not self.head or not self.tail:
            return

        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = node.child
            self.head.parent = None
            
        elif node == self.tail:
            self.tail = node.parent
            self.tail.child = None

        else:
            node.parent.child = node.child
            node.child.parent = node.parent

        length -= 1


    def __iter__(self):
        return self


    def __next__(self):

        if not self.iteration:
            self.iteration = self.head
            raise StopIteration()

        iteration_value = self.iteration
        self.iteration = self.iteration.child
        return iteration_value



class Stack(Chain):

	def __init__(self, array=None):
		super().__init__(array)


	def push(self, value):
		node = Node(value, self.tail)		

		if self.tail:
			self.tail.child = node
		else:
			self.head = node
		
		self.tail = node

	
	def pull(self):
		
		if self.tail:
			value = self.tail.value
			self.tail = self.tail.parent

			if self.tail:
				self.tail.child = None
			else:
				self.head = None
			
			return value

		else:
			return	

