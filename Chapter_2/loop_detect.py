# Given a Linked List which might contain a loop, return the node at beginning of loop

from class_linked_list import LinkedList

A = LinkedList("A")
B = LinkedList("B")
C = LinkedList("C")
D = LinkedList("D")
E = LinkedList("E")

A.set_next(B)
B.set_next(C)
C.set_next(D)
D.set_next(E)
E.set_next(C)

head = A

def loop_detect(head):
    slow = head
    fast = head 

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None

print(loop_detect(head).item)