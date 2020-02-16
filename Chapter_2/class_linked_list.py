class LinkedList:

    def __init__(self, item):
        self.item = item
        self.next = None

    def set_next(self, node):
        self.next = node

def print_list(list):
    i = 0
    while list and i < 20:
        print(list.item, end="")
        if list.next:
            print(" -> ", end="")
        i += 1
        list = list.next
    print()