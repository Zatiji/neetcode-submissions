class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node(-1, None, None)
        self.tail = Node(-1, None, None)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def isEmpty(self) -> bool:
        return self.size <= 0

    def append(self, value: int) -> None:
        end_node = self.tail.prev
        new_node = Node(value, self.tail, end_node)
        end_node.next = new_node
        self.tail.prev = new_node

        self.size += 1

    def appendleft(self, value: int) -> None:
        first_node = self.head.next
        new_node = Node(value, first_node, self.head)
        first_node.prev = new_node
        self.head.next = new_node

        self.size += 1

    def pop(self) -> int:
        if self.size <= 0:
            return -1

        res = self.tail.prev
        new_end = self.tail.prev.prev
        new_end.next = self.tail
        self.tail.prev = new_end

        self.size -= 1
        return res.val

    def popleft(self) -> int:
        if self.size <= 0:
            return -1

        res = self.head.next
        new_start = self.head.next.next
        new_start.prev = self.head
        self.head.next = new_start

        self.size -= 1
        return res.val
        
