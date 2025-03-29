class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        first_pointer = self.head

        second_pointer = self.head

        for i in range(k):
            second_pointer = second_pointer.next

        while second_pointer is not None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        return first_pointer


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(8)
