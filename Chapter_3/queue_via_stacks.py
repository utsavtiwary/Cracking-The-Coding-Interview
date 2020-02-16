from class_stack import Stack

class MyQueue:

    def __init__(self):
        self.stack_oldest = Stack()
        self.stack_newest = Stack()

    def __shift_stacks(self):
        if self.stack_oldest.isEmpty():
            while not self.stack_newest.isEmpty():
                self.stack_oldest.push(self.stack_newest.pop())

    def add(self, item):
        self.stack_newest.push(item)

    def remove(self):
        if self.size() == 0:
            return None

        self.__shift_stacks()
        return self.stack_oldest.pop()

    def peek(self):
        if self.size() == 0:
            return None

        self.__shift_stacks()
        return self.stack_oldest.peek()

    def size(self):
        return self.stack_oldest.length + self.stack_newest.length

if __name__ == "__main__":
    # TEST
    my_queue = MyQueue()
    my_queue.add(1)
    my_queue.add(2)
    my_queue.add(3)
    print(my_queue.remove())
    print(my_queue.remove())
    print(my_queue.remove())
    print(my_queue.remove())