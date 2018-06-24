from _tree import root

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)


print("in-order " + "=" * 10)
in_order(root)
print("post-order " + "=" * 10)
post_order(root)
