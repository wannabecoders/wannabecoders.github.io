from _tree import root

# pre-order
def traverse(root):
    if not root:
        return
    print(root.val)
    traverse(root.left)
    traverse(root.right)

traverse(root)
