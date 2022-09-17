
class Node:

    def __init__(self, value, parent=None, child=None):

        self.value = value
        self.parent = parent
        self.child = child


    def __str__(self):
        return f"Node({self.value})"


class Chain:

    def __init__(self, contents=None):
        
        if contents:
            
            current = None 
            for i, value in enumerate(contents):    
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
        output = ""

        current = self.head
        while current:
            output += f"{current.value}{' > ' if current != self.tail else ''}"
            current = current.child

        return output

