class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumValues = []

    def push(self, val: int) -> None:
        if  len(self.minimumValues) == 0 or val <= self.minimumValues[-1]:
            self.minimumValues.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.minimumValues[-1] == self.stack[-1]:
            self.minimumValues.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimumValues[-1]

        
