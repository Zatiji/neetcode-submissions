# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        left = None
        curr = head
        right = head.next

        while curr is not None:
            curr.next = left

            left = curr
            curr = right
            if right is not None:
                right = right.next
        
        return left

        