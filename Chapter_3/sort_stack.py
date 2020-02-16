from class_stack import Stack

class SortStack:

    def __init__(self):
        self.sorted = Stack()
        self.temp = Stack()

    def push(self, item):
        if self.sorted.isEmpty():
            self.sorted.push(item)
        while not self.sorted.isEmpty() and self.sorted.peek() < item:
            self.temp.push(self.sorted.pop())
        self.sorted.push(item)
        while not self.temp.isEmpty():
            self.sorted.push(self.temp.pop())

    def pop(self):
        if self.sorted.isEmpty():
            return None
        return self.sorted.pop()

    def peek(self):
        if self.sorted.isEmpty():
            return None
        return self.sorted.peek()

    def isEmpty():
        return self.sorted.isEmpty()

if __name__ == "__main__":
    # TEST
    sort_stack = SortStack()
    sort_stack.push(4)
    sort_stack.push(2)
    sort_stack.push(3)
    sort_stack.push(5)
    print(sort_stack.pop())
    print(sort_stack.pop())
    print(sort_stack.pop())


