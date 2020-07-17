class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # question: why are we passing in node and prev when this is already
        # called on an isntance of a linked list?

        prev = None
        current = self.head
        while current is not None:
            # save next and reverse current node
            next = current.get_next()
            current.set_next(prev)
            # move pointers for next loop
            prev = current
            current = next
        # Update head pointer to the last node we saw
        self.head = prev
