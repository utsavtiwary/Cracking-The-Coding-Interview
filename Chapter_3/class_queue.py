from class_list_node import ListNode

class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        new_node = ListNode(item)
        if self.last:
            self.last.next = new_node
        self.last = new_node
        if not self.first:
            self.first = new_node

    def remove(self):
        if not self.first:
            return None
        output = self.first.item
        self.first = self.first.next
        if not self.first:
            self.last = None
        return output

    def peek(self):
        if self.first:
            return self.first.item
        return None

    def isEmpty(self):
        return not self.first

if __name__ == "__main__":
    # TEST
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)

    print(queue.remove())
    print(queue.peek())
    print(queue.remove())
    print(queue.isEmpty())