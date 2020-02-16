from class_list_node import ListNode

class Stack:

    def __init__(self):
        self.top = None
        self.length = 0

    def pop(self):
        if not self.top:
            return None
        output = self.top.item
        self.top = self.top.next
        return output

    def push(self, item):
        new_top = ListNode(item)
        new_top.next = self.top
        self.top = new_top

    def peek(self):
        if not self.top:
            return None
        return self.top.item

    def isEmpty(self):
        return self.top is None

# TEST
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.isEmpty())