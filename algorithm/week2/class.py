
class Person:
    def __init__(self, name_param):
        self.name = name_param
        print(f"hihi i am created  {name_param}",self)


    def talk(self,another_name):
        print(f"안녕하세요 저는 {self.name} 이무니다 또한 {another_name}")

person_1 = Person("유재석")

person_2 = Person("박명수")

person_1.talk("헬로우")


class Node:

    def __init__(self , data):
        self.data = data
        self.next = None



node = Node(1)

node2 = Node(2)

node3 = Node(3)

node.next = node3

node3.next = node2
