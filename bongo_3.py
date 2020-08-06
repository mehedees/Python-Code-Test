from typing import List

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def find_ancestor(node: Node, path: List):
    if node.parent:
        path.append(node.value)
        return find_ancestor(node.parent, path)
    else:
        path.append(node.value)


def lca(node_1: Node, node_2: Node):
    node_1_path = []
    find_ancestor(node_1, node_1_path)
    node_2_path = []
    find_ancestor(node_2, node_2_path)
    node_1_path.reverse()
    node_2_path.reverse()
    lca = 0
    for i in range(0, len(node_1_path) if len(node_1_path) < len(node_2_path) else len(node_2_path)):
        if node_1_path[i] != node_2_path[i]:
            break
        else:
            lca = node_1_path[i]

    print(lca)
    return lca


if __name__ == "__main__":
    n1 = Node(1, None)
    n2 = Node(2, n1)
    n3 = Node(3, n1)
    n4 = Node(4, n2)
    n5 = Node(5, n2)
    n6 = Node(6, n3)
    n7 = Node(7, n3)
    n8 = Node(8, n4)
    n9 = Node(9, n4)
    lca(n3, n7)
