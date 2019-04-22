class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


def dfs_inorder(node):
    if not node:
        return

    dfs_inorder(node.left)
    print(node.key)
    dfs_inorder(node.right)


def dfs_preorder(node):
    if not node:
        return

    print(node.key)
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_preorder(node):
    if not node:
        return

    print(node.key)
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_postorder(node):
    if not node:
        return

    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.key)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    dfs_inorder(root)
    print('-----------')
    dfs_preorder(root)
    print('------------')
    dfs_postorder(root)
