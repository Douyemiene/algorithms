class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
      


index_of_nodes = ['4', '-1', '4', '1', '1']
nodes = [None] * len(index_of_nodes)

for index, data in enumerate(index_of_nodes):
    nodes[index] = Node(data, None, None)


