class Node:
    def __init__(self, val, left=None, right=None, num_nodes: int = 1):
        self.val = val
        self.left = left
        self.right = right
        self.num_nodes = num_nodes


def count_smaller_to_right(nums: list[int]) -> list[int]:
    counts = [0] * len(nums)
    avl_tree = Node(nums[-1])
    for i in range(len(nums) - 2, -1, -1):
        avl_tree, counts[i] = avl_insert(Node(nums[i]), avl_tree)
    return counts


def avl_insert(insert_node: Node, tree: Node) -> tuple[Node, int]:
    node = tree
    smaller_node_count = 0
    while True:
        node.num_nodes += 1
        if insert_node.val >= node.val:
            smaller_node_count += (0 if insert_node.val == node.val else 1) + (node.left.num_nodes if node.left is not None else 0)
            if node.right is not None:
                node = node.right
            else:
                node.right = insert_node
                break
        else:
            if node.left is not None:
                node = node.left
            else:
                node.left = insert_node
                break
    return balance_avl_tree(tree)[0], smaller_node_count


def balance_avl_tree(tree: Node) -> tuple[Node, int]:
    left_subtree, left_height = balance_avl_tree(tree.left) if tree.left is not None else (None, 0)
    right_subtree, right_height = balance_avl_tree(tree.right) if tree.right is not None else (None, 0)
    height_difference = left_height - right_height
    if height_difference > 1:
        if left_subtree.left is None:
            left_subtree.num_nodes -= left_subtree.right.num_nodes
            left_subtree = rotate_left(left_subtree, left_subtree.right)
            left_subtree.num_nodes += left_subtree.left.num_nodes
        tree.num_nodes += (
                              left_subtree.right.num_nodes if left_subtree.right is not None else 0) - left_subtree.num_nodes
        left_subtree.num_nodes += 1 + (tree.right.num_nodes if tree.right is not None else 0)
        tree = rotate_right(tree, left_subtree)
        left_height -= 1
        right_height += 1
    elif height_difference < -1:
        if right_subtree.right is None:
            right_subtree.num_nodes -= right_subtree.left.num_nodes
            right_subtree = rotate_right(right_subtree, right_subtree.left)
            right_subtree.num_nodes += right_subtree.right.num_nodes

        tree.num_nodes += (
                              right_subtree.left.num_nodes if right_subtree.left is not None else 0) - right_subtree.num_nodes
        right_subtree.num_nodes += 1 + (tree.left.num_nodes if tree.left is not None else 0)
        tree = rotate_left(tree, right_subtree)
        left_height += 1
        right_height -= 1
    else:
        tree.left = left_subtree
        tree.right = right_subtree
    return tree, 1 + max(left_height, right_height)


def rotate_right(root: Node, left_subtree: Node) -> Node:
    left_subtree.right, root.left = root, left_subtree.right
    return left_subtree


def rotate_left(root: Node, right_subtree: Node) -> Node:
    right_subtree.left, root.right = root, right_subtree.left
    return right_subtree


if __name__ == "__main__":
    print(count_smaller_to_right([5, 2, 6, 1]))  # ANS = [2, 1, 1, 0]
    print(count_smaller_to_right([65, 36, 100, 41]))  # ANS = [2,0,1,0]
    print(count_smaller_to_right([1, 9, 7, 8, 5]))  # ANS = [0,3,1,1,0]
    print(count_smaller_to_right([28, 94, 13, 2, 97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100,
                                  41]))  # ANS = [5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
    print(count_smaller_to_right(
        [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97,
         3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100,
         41]))  # ANS = [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
