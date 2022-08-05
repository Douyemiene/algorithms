import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
      


def create_tree(index_of_nodes):
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

    return [nodes, index_of_root]


def height(node):
    if node == None:
        return 0

    children = [None] * len(node.children)

    if children == []:
        return 1

    for i, child in enumerate(node.children):
        children[i] = height(child)

    return 1 + max(children)





def main():
  n = int(sys.stdin.readline())
  numbers = list(map(int, sys.stdin.readline().split()))
  tree, index_of_root = create_tree(numbers) 
  print(height(tree[index_of_root]))

threading.Thread(target=main).start()