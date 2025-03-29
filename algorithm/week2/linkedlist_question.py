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


def get_linked_list_sum(linked_list_1: LinkedList, linked_list_2: LinkedList):
    value1 = ""

    value2 = ""

    cur_node_of_list_1 = linked_list_1.head

    while cur_node_of_list_1.next is not None:
        value1 += str(cur_node_of_list_1.data)
        cur_node_of_list_1 = cur_node_of_list_1.next
    
    value1 += str(cur_node_of_list_1.data)

    cur_node_of_list_2 = linked_list_2.head

    while cur_node_of_list_2.next is not None:
        print(cur_node_of_list_2.data)
        value2 += str(cur_node_of_list_2.data)
        cur_node_of_list_2 = cur_node_of_list_2.next

    value2 += str(cur_node_of_list_2.data)


    return int(value1) + int(value2)



linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))