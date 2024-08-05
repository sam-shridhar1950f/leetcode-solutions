class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val     # Holds the value or data of the node
        self.next = next  # Points to the next node in the linked list; default is None

def swap_linked_list_nodes(head, start, end):
    
    if start == end:
        return head
    
    if not head:
        return None

    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    curr = head
    c = -1 

    prevStart = None
    startNode = None
    afterStart = None

    prevEnd = None
    endNode = None
    afterEnd = None
    

    while curr:
        c += 1
        if c == start - 1:
            prevStart = curr
        elif c == start:
            startNode = curr
            afterStart = curr.next
        elif c == end - 1:
            prevEnd = curr
        elif c == end:
            endNode = curr
            afterEnd = curr.next

        curr = curr.next

    # reassigning end node
    if prevStart:
        prevStart.next = endNode
    if endNode:
        endNode.next = afterStart

    # reassigning startNode
    if prevEnd:
        prevEnd.next = startNode
    if startNode:
        startNode.next = afterEnd

    if start == 0:
        head = endNode

    return head
            
            
        
    
    
    
    pass
