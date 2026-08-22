class DynamicArray:
    
    def __init__(self, capacity: int):
        self.a = []
        self.size = 0

        for i in range(capacity):
            self.a.append(0)
        
    def get(self, i: int) -> int:
        print(self.a)
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= len(self.a):
            self.resize()
        
        self.a[self.size] = n
        self.size += 1


    def popback(self) -> int:
        element = self.a[self.size - 1]
        self.set(self.size - 1, 0)
        self.size -= 1
        return element

    def resize(self) -> None:
        actual_capacity = self.getCapacity()

        for i in range(actual_capacity):
            self.a.append(0)


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.a)
