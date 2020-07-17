"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            if self.left:
                # Insert into left subtree
                self.left.insert(value)
            else:
                # Create new node
                self.left = BSTNode(value)

        # Case 2: value is greater than or equal to self.value
        else:
            if self.right:
                # Insert into right subtree
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            # target found, return True
            return True
        elif target < self.value:
            # Less than, search left subtree
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target >= self.value:
            # Greater than or equal, search right subtree
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # The right-most node will be max, find it and return the value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn, order="inorder"):
        """
        Calls a function (fn) on all values in this binary search tree.

        order (str): The order in which to traverse the tree.  Options are 
                     "inorder", "preorder" and "postorder"
        """
        if order == "inorder":
            # Call fn on left subtree, then this node, then right subtree
            if self.left:
                self.left.for_each(fn, order)
            fn(self.value)
            if self.right:
                self.right.for_each(fn, order)
        elif order == "preorder":
            # Call fn on this node, then left subtree and right subtree
            fn(self.value)
            if self.left:
                self.left.for_each(fn, order)
            if self.right:
                self.right.for_each(fn, order)
        elif order == "postorder":
            # Call fn on left subtree and right subtree, then this node
            if self.left:
                self.left.for_each(fn, order)
            if self.right:
                self.right.for_each(fn, order)
            fn(self.value)
        else:
            raise Warning(f'Unrecognized order parameter: "{order}"\n\tOptions are "inorder", "preorder" and "postorder"')

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        self.for_each(fn=lambda x: print(x), order="inorder")

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # set up a queue to hold items as we traverse
        q = queue.Queue()
        q.put(node)
        # while there are items in the queue
        while q.qsize() > 0:
            # get and print the next node
            current = q.get()
            print(current.value)
            # enqueue the left and right children of that node
            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # store nodes in a stack as we traverse
        stack = [node]
        while len(stack) > 0:
            # pop off next item and print it
            current = stack.pop()
            print(current.value)
            # add left and right children of that node to the stack
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        self.for_each(fn=lambda x: print(x), order="preorder")

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        self.for_each(fn=lambda x: print(x), order="postorder")
