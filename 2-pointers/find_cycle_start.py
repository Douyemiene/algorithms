class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, node):
        self.next = node


def node_pointers_meet_in_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return fast

    return None

# 1 2 3 4 5 6 - 1
def get_cycle_start(head, length_of_cycle):
    first = head
    second = head

    for _ in range(length_of_cycle):
        second = second.next

    if second == head:
        return head

    while True:
        first = first.next
        second = second.next

        if first == second:
            return first


def get_cycle_length(node_in_cycle):
    current = node_in_cycle.next 
    cycle_length = 1

    while current != node_in_cycle:
        current = current.next 
        cycle_length += 1  

    return cycle_length


def find_cycle_start(head):
    node_pointers_meet = node_pointers_meet_in_cycle(head)

    if node_pointers_meet == None:
        return None

    length_of_cycle = get_cycle_length(node_pointers_meet)

    return get_cycle_start(head, length_of_cycle)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
