from collections import defaultdict

def counter():
    count = 0
    while True:
        count += 1
        yield count


class Node:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_unival(memo, node: Node, val) -> bool:
    if id(node) in memo.keys():
        return memo[id(node)]
    elif node is None or (node.val == val and is_unival(memo, node.left, val) and is_unival(memo, node.right, val)):
        memo[id(node)] = True
        return True
    else:
        return False


if __name__ == "__main__":
    root = None
    count = 0
    memo = {}
    root = Node(0,
                left=Node(1),
                right=Node(0,
                           left=Node(1,
                                     left=Node(1),
                                     right=Node(1)),
                           right=Node(0)))
    # DFS
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node is None:
            pass
        elif is_unival(memo, node, node.val):
            count += 1
            stack.append(node.left)
            stack.append(node.right)
        else:
            stack.append(node.left)
            stack.append(node.right)

    print(count)