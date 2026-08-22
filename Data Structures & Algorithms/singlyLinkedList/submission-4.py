class Node:
    def __init__(self, val: int, next_node: Node):
        self.value = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        counter = 0
        curr = self.head

        while curr and (counter < index):
            curr = curr.next_node
            counter += 1

        if not curr:
            return -1
        else:
            return curr.value 

    def insertHead(self, val: int) -> None:
        old_second = self.head
        self.head = Node(val, old_second)

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, None)
            return
        
        curr = self.head
        while curr.next_node:
            curr = curr.next_node
        
        curr.next_node = Node(val, None)
        
    def remove(self, index: int) -> bool:
        if not self.head:
            return False
    
        slow = self.head
        fast = self.head.next_node
        counter = 1

        if index == 0:
            self.head = fast
            return True

        while fast and counter < index:
            slow = fast
            fast = fast.next_node
            counter += 1
        
        if not fast:
            return False
        else:
            slow.next_node = fast.next_node
            return True



    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.value)
            curr = curr.next_node
    
        return res
        
