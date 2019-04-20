class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder_traversal(node):
    if not node:
        return

    inorder_traversal(node.left)
    print(node.key, end=" ")
    inorder_traversal(node.right)


def insert_at_empty_space(node, key):

    q = []
    q.append(node)

    while len(q):
        temp = q.pop(0)

        if not temp:
            return

        if not temp.left:
            temp.left = Node(key)
            return

        if not temp.right:
            temp.right = Node(key)
            return

        q.extend([temp.left, temp.right])


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder_traversal(root)

    key = 'x'
    insert_at_empty_space(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder_traversal(root)
