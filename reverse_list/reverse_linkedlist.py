class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr != None:
            next_node_to_process = curr.next
            curr.next = prev
            prev = curr
            curr = next_node_to_process

        return prev
