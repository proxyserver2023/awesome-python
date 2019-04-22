class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


def bfs(node):
    if not node:
        return

    q = []
    q.append(node)

    while len(q):
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        print(temp.key, end=' ' if len(q) else '')


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    bfs(root)
