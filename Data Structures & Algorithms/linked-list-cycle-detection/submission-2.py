# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        turtle = head
        rabbit = head.next

        while (turtle and rabbit):
            if turtle == rabbit:
                return True
            
            
            turtle = turtle.next

            if rabbit.next:
                rabbit = rabbit.next.next
            else:
                rabbit = rabbit.next

        return False

        