# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size <= 1:
            return None

        index = size - n
        previous = head

        if index == 0:
            return head.next

        for _ in range(index-1):
            previous = previous.next
        
        nodeToRemove = previous.next
        if nodeToRemove:
            previous.next = nodeToRemove.next
            nodeToRemove.next = None
        else:
            previous.next = None

        return head


        