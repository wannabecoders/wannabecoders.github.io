from _tree import root

def traverse(root):
    stack = []
    push(root, stack)
    while stack:
        op, node = stack.pop()
        if not node:
            continue
        if op == 't':
            push(node, stack)
        else:
            print(node.val)

def push(node, stack):
    stack.append(('t', node.right))
    stack.append(('t', node.left))
    stack.append(('p', node))

traverse(root)
