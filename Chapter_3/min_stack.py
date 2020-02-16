
class MinStack:

    class StackNode:

        def __init__(self, item):
            self.item = item
            self.next = None
            self.next_min = None

    def __init__(self):
        self.top = None
        self.min = None

    def push(self, item):
        new_node = self.StackNode(item)
        if self.top:
            if item <= self.min:
                new_node.next_min = self.min
                self.min = item
            new_node.next = self.top
            self.top = new_node
        else:
            self.min = item
            self.top = new_node

    def pop(self):
        if not self.top:
            return None
        top_node = self.top
        if top_node.item == self.min:
            self.min = top_node.next_min
        self.top = top_node.next
        return top_node.item

    def get_min(self):
        return self.min


min_stack = MinStack()
min_stack.push(4)
min_stack.push(2)
min_stack.push(2)
min_stack.push(3)

print(min_stack.get_min())
min_stack.pop()
min_stack.pop()
print(min_stack.get_min())
min_stack.pop()
print(min_stack.get_min())
min_stack.pop()
print(min_stack.get_min())