
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    serialized_arr = []
    queue = [(0, root)]
    while queue:
        index, node = queue.pop(0)
        if node is not None:
            serialized_arr.append((index, node.value))
            left_child_index = 2 * index + 1
            right_child_index = left_child_index + 1
            queue.append((left_child_index, node.left))
            queue.append((right_child_index, node.right))

    return str(serialized_arr)


def deserialize(serialized_str: str) -> Node:
    serialized_arr = list(map(lambda x: tuple(map(lambda y: int(y), x.replace("(", "").replace(")","").split(", "))), serialized_str[1:-1].split("), ")))
    serialized_dict = {key: value for key, value in serialized_arr}
    print(serialized_arr)
    print(serialized_dict)
    if not serialized_arr:
        return None
    else:
        root = Node(serialized_dict[0])
    queue = [(0, root)]

    while queue:
        index, node = queue.pop(0)

        left_child_index = 2 * index + 1
        right_child_index = left_child_index + 1

        if left_child_index in serialized_dict.keys():
            node.left = Node(serialized_dict[left_child_index])
            queue.append((left_child_index, node.left))
        if right_child_index in serialized_dict.keys():
            node.right = Node(serialized_dict[right_child_index])
            queue.append((right_child_index, node.right))

    return root


r = Node(1,
         Node(2),
         Node(3,
              Node(4,
                   Node(6),
                   Node(7)),
              Node(5)))

s = serialize(None)
#s = "[1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, None, None]"
print(s)
r = deserialize(s)

print(serialize(r))
