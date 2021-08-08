def reverseList(self, head):
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next # Remember next node [1, 2, 3]
        curr_node.next = prev_node  # REVERSE! None, first time round.
        prev_node = curr_node  # Used in the next iteration.
        curr_node = next_node  # Move to next node.
    head = prev_node
    return head