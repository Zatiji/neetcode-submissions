# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        resultHead = ListNode(0, None)
        response = resultHead

        remainder = 0
        while l1 and l2:
            result = ((l1.val + l2.val)) + remainder
            response.next = ListNode(result%10, None)

            remainder = result // 10
            print(result)
            print(remainder)

            l1 = l1.next
            l2 = l2.next
            response = response.next
        
        if l1 and not l2:
            response.next = l1
        elif l2 and not l1:
            response.next = l2

        while remainder > 0:
            if not response.next:
                response.next = ListNode(remainder)
                remainder = 0

            else:
                result = response.next.val + remainder
                response.next.val = result % 10
                remainder = result // 10
                response = response.next
        
        return resultHead.next


