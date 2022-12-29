class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def set_next(self, node):
        self.next = node

 # 1 - 2 - 3 - 4 - 2
def node_pointers_meet_in_cycle(head):
    slow = head.next 
    fast = head.next.next 
    
    while fast != slow:
            slow = slow.next 

            if fast.next == None:
                return None
            fast = fast.next.next 

    return fast


def find_cycle_start():
    # one,
    # check if there is a cycle
        # yes? -> return the node where the cycle occurs (node_pointers_meet)
            # get two pointers, place one at the head of our list
            # make the other point to node_pointers_meet
            # update pointers to point to their adjacent node
            # till both are at the same node (the start of the cycle)
        # no? -> return None
    pass

def main():
    node4 = Node(4, None)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    head = Node(1, node2)
    node4.next = node2
    # node6 = Node(6, None)
    # node5 = Node(5, node6)
    # node4 = Node(4, node5)
    # node3 = Node(3, node4)
    # node2 = Node(2, node3)
    # head = Node(1, node2)


    # current = head
    # while current != None:
    #     print(f'{current.value}')
    #     current = current.next
    node_pointers_meet = node_pointers_meet_in_cycle(head)
    print(node_pointers_meet.value)
    

main()