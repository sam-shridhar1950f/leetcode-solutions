# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        c = 0
        while curr != None:
            c += 1
            curr = curr.next

        print(f"size: {c}")
        
        curr = head
        idx = c - n
        print(f"index to remove: {idx}")
        p = -1
        while curr != None:
            p += 1
            if idx == 0:
                print(f"current 0th index: {curr.val}")
                head = head.next # remove first value of linked list
                break
            elif p == idx - 1:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next


        return head




        
