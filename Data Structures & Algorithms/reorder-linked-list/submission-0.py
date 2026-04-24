# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_dict = {}
        size = 0

        curr = head
        idx = 0
        while curr:
            size += 1
            node_dict[idx] = curr
            curr = curr.next
            idx += 1
        
        curr = head
        curr_next = curr.next
        idx_dict = size - 1

        for i in range(1, size): # we start at 1 because we don't want tomess with the head
            if i % 2 != 0:
                curr.next = node_dict[idx_dict]
                idx_dict -= 1
                curr = curr.next
            else:
                curr.next = curr_next
                curr_next = curr_next.next
                curr = curr.next
        
        curr.next = None
        


        