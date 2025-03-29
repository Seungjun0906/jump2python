class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node  = Node(3)

class LinkedList:

    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        # 헤드 밖에 없으면 ㅇㅇ
        
        while cur.next is not None:
            cur = cur.next
        
        print(cur.data)
        cur.next = Node(value)

    def print_all (self):
        cur = self.head

        list = []

        while cur is not None:
            list.append(cur.data)

            cur = cur.next

        print(list)
        

    def get_node(self, index:int):
        cur_index = 0
        cur_node = self.head

        while cur_index != index:
            cur_index += 1
            if cur_node.next is not None:
                cur_node = cur_node.next
            else:
                raise Exception("존재하지 않는 인덱스입니다.")
        
        return cur_node
    

    def add_node (self, index:int, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head

            self.head = new_node
            return

        prev = self.get_node(index -1)

        next_node = prev.next
        
        new_node.next = next_node

        prev.next = new_node

    def delete_node (self, index:int ):
        
        if index == 0:
            self.head = self.head.next
            return

        
        node = self.get_node(index-1)
        node.next = node.next.next

    





     

            
            

        
        
    


linked_list = LinkedList("1번 노드")

linked_list.append("2번 노드")
linked_list.append("3번 노드")
linked_list.append("4번 노드")
linked_list.append("5번 노드")
linked_list.append("6번 노드")
linked_list.append("7번 노드")

linked_list.add_node(0,"여기는 원래 1번자리였으셈")

linked_list.delete_node(1)

linked_list.print_all()
