
class MultiStack:

    class StackInfo:

        def __init__(self, start, capacity):
            self.size = 0
            self.start = start
            self.capacity = capacity

        def is_full(self):
            return self.size == self.capacity

        def is_empty(self):
            return self.size == 0

        def last_element_index(self, max_index):
            return (self.start + self.size - 1) % max_index

        def last_capacity_index(self, max_index):
            return (self.start + self.capacity - 1) % max_index


    def __init__(self, capacity=20, stacks=3):
        self.stack_infos = []
        for i in range(stacks):
            self.stack_infos.append(self.StackInfo(i * capacity, capacity))
        self.values = [None] * stacks * capacity

    def push(self, stack_num, item):
        if stack_num >= len(self.stack_infos):
            return
        if self.__all_stacks_full():
            return

        stack = self.stack_infos[stack_num]
        if stack.is_full():
            self.__expand(stack_num)

        stack.size += 1
        self.values[stack.last_element_index(len(self.values))] = item

    def pop(self, stack_num):
        if stack_num >= len(self.stack_infos):
            return None
        stack = self.stack_infos[stack_num]
        if stack.is_empty():
            return None

        top_index = stack.last_element_index(len(self.values))
        item = self.values[top_index]
        self.values[top_index] = 0
        stack.size -= 1
        return item

    def peek(self, stack_num):
        if stack_num >= len(self.stack_infos):
            return None
        stack = self.stack_infos[stack_num]
        if stack.is_empty():
            return None

        top_index = stack.last_element_index(len(self.values))
        return self.values[top_index]

    def is_Empty(self, stack_num):
        if stack_num >= len(self.stack_infos):
            return None
        stack = self.stack_infos[stack_num]
        return stack.is_empty():

    def __expand(self, stack_num):
        self.__shift((stack_num + 1) % len(self.stack_infos))
        self.stack_infos[stack_num].capacity += 1

    def __shift(self, stack_num):
        stack = self.stack_infos[stack_num]

        if stack.is_full():
            next_stack = (stack_num + 1) % len(self.stack_infos)
            self.__shft(next_stack)
            stack.capacity += 1

        index = stack.last_capacity_index(len(self.values))
        for i in range(stack.capacity):
            self.values[index] = self.values[(index - 1) % len(self.values)]
            index = (index - 1) % len(self.values)

        self.values[stack.start] = 0
        stack.start = (stack.start + 1) % len(self.values)
        stack.capacity -= 1


    def __all_stacks_full(self):
        return len(self.values) == self.__number_of_elements()

    def __number_of_elements(self):
        total = 0
        for stack in self.stack_infos:
            total += stack.size
        return total

if __name__ == "__main__":
    # TEST
    stack = MultiStack(capacity=1)
    stack.push(1, 5)
    stack.push(1, 2)
    stack.push(2, 3)
    stack.pop(1)
    stack.pop(2)
    stack.peek(1)

for i in stack.values:
    print(i)
