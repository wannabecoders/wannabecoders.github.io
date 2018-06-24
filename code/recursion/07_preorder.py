from _tree import root

# pre-order
def traverse(root, acc):
    if not root:
        return acc
    acc.append(root.val)
    traverse(root.left, acc)
    traverse(root.right, acc)
    return acc

print(traverse(root, []))
