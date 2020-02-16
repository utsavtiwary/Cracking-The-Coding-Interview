# Given 2 numbers represented by linked lists, add the numbers and return as linked list
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2), i.e. 617 + 295
# Output: 2 -> 1 -> 9, i.e. 912

from class_linked_list import LinkedList, print_list

def get_length(list):
    count = 0
    while list:
        count += 1
        list = list.next
    return count

def elongate(list, by):
    point = list
    while point.next:
        point = point.next

    dummy = LinkedList(0)
    point2 = dummy
    for i in range(by):
        point2.next = LinkedList(0)
        point2 = point2.next

    point.next = dummy.next
    return list

def sum_lists(l1, l2):

    if not l1:
        return l2
    if not l2:
        return l1

    len_l1 = get_length(l1)
    len_l2 = get_length(l2)

    longer = l1 if len_l1 >= len_l2 else l2
    shorter = l2 if len_l1 >= len_l2 else l1

    shorter = elongate(shorter, abs(len_l1 - len_l2))
    output = longer
    carry = 0

    for i in range(max(len_l1, len_l2)):
        sum_dig = shorter.item + output.item + carry
        carry = sum_dig // 10
        digit = sum_dig % 10
        output.item = digit

        if i < max(len_l1, len_l2) - 1:
            shorter = shorter.next
            output = output.next

    if carry > 0:
        output.next = LinkedList(carry)

    return longer

if __name__ == "__main__":
    # TEST
    first_1 = LinkedList(7)
    first_2 = LinkedList(1)
    first_3 = LinkedList(6)

    sec_1 = LinkedList(5)
    sec_2 = LinkedList(9)
    sec_3 = LinkedList(2)

    first_1.next, first_2.next, sec_1.next, sec_2.next = first_2, first_3, sec_2, sec_3

    output = sum_lists(first_1, sec_1)
    print_list(output)



