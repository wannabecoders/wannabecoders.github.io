class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.val = n

"""
      1
     / \
    2   3
   / \  / \
  4  5  6  7
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
