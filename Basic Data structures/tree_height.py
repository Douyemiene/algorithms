class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
      


index_of_nodes = [-1, 0, 4, 0, 3]
nodes = [None] * len(index_of_nodes)

index_of_root = None

for index in range(len(nodes)):
    nodes[index] = Node(index)

for index, node in enumerate(nodes):
    index_of_parent =  index_of_nodes[index]

    if index_of_parent == -1:
        index_of_root = index
        continue

    parent = nodes[ index_of_parent ]

    parent.children.append(node)


def height(node):
    if node == None:
        return 0

    children = [None] * len(node.children)

    if children == []:
        return 1

    for i, child in enumerate(node.children):
        children[i] = height(child)

    return 1 + max(children)


print(f'root {index_of_root}')

print(height(nodes[index_of_root]))