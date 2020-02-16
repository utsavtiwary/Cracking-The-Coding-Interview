from class_stack import Stack

class StackOfPlates:

    def __init__(self, threshold=20):
        self.stack_list = []
        self.threshold = threshold

    def push(self, item):
        if len(self.stack_list) == 0 or self.stack_list[-1].length == self.threshold:
            new_stack = Stack()
            new_stack.push(item)
            self.stack_list.append(new_stack)
            return
        self.stack_list[-1].push(item)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        item = self.stack_list[-1].pop()
        while len(self.stack_list) > 0 and self.stack_list[-1].length == 0:
            self.stack_list.pop()
        return item

    def pop_at(self, stack_num):
        if stack_num >= len(self.stack_list):
            return None
        stack = self.stack_list[stack_num]
        if stack.isEmpty():
            return None

        item = self.stack_list[stack_num].pop()
        return item

    def peek(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list[-1].peek()

    def isEmpty(self):
        return len(self.stack_list) == 0


if __name__ == "__main__":
    # TEST
    stack_of_plates = StackOfPlates(2)
    stack_of_plates.push(1)
    stack_of_plates.push(2)
    stack_of_plates.push(3)
    stack_of_plates.push(4)
    stack_of_plates.push(5)

    while not stack_of_plates.isEmpty():
        print("Popped: ", stack_of_plates.pop())
        print("Number of Stacks: ", len(stack_of_plates.stack_list))

    stack_of_plates.push(1)
    stack_of_plates.push(2)
    stack_of_plates.push(3)
    stack_of_plates.pop_at(0)

    stack_of_plates.pop()
    print(stack_of_plates.peek())