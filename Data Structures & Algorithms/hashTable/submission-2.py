class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __repr__(self):
        return f"({self.key} -> {self.val})"

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = [None] * capacity


    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity

        if not self.arr[index]:
            self.arr[index] = Pair(key, value)
            self.size += 1
        else:
            if self.arr[index].key == key:
                self.arr[index].val = value
            else:
                pair = self.arr[index]
                while pair.next:
                    pair = pair.next

                pair.next = Pair(key, value)
                self.size += 1

        if self.size >= (self.capacity / 2):
            self.resize()


    def get(self, key: int) -> int:
        index = key % self.capacity

        pair = self.arr[index]
        while pair and key != pair.key:
            pair = pair.next
        
        if not pair:
            return -1
        else:
            return pair.val


    def remove(self, key: int) -> bool:
        index = key % self.capacity

        if not self.arr[index]:
            return False
        
        pair = self.arr[index]
        if pair.key == key:
            self.arr[index] = None
            self.size -= 1
            return True

        while pair.next and pair.next.key != key:
            pair = pair.next

        if not pair.next:
            return False
        else:
            pair.next = pair.next.next
            self.size -= 1
            return True
    

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        new_arr = []
        self.capacity *= 2

        for i in range(self.capacity):
            new_arr.append(None)
        
        for pair in self.arr:
            if pair:
                new_index = pair.key % self.capacity
                new_arr[new_index] = pair
        
        self.arr = new_arr

