class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
      


index_of_nodes = [4, -1, 4, 1, 1]
nodes = [None] * len(index_of_nodes)


for index in range(len(nodes)):
    nodes[index] = Node(index)

for index, node in enumerate(nodes):
    index_of_parent =  index_of_nodes[index]
    parent = nodes[ index_of_parent ]

    parent.children.append(node)

print(nodes[4].data)


for n in nodes[4].children:
    print('data',n.data)