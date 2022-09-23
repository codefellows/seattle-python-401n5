class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        # LL  [Roger] -> [Brendon] -> [Brian] -> [Jae] -> [JJ] -> None
        # Insert Roger
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        pass

    def to_string(self):
        pass

    # def travel_ll(self):
    #     current = self.head
    #     while current:
    #         print(current.value)
    #         current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    # LL [5] -> None
    ll.insert(6)
    # LL [6] -> [5] -> None
    ll.insert(7)
    # LL [7] -> [6] -> [5] -> None
    # ll = LinkedList()
    # brendon = Node(1)
    # brian = Node(2)
    # jae = Node(3)
    # jj = Node(4)
    # roger = Node(5)
    # brendon.next = brian
    # brian.next = jae
    # jae.next = jj
    # ll.head = brendon
    # ll.travel_ll()

#                                            current
# LL  [Brendon] -> [Brian] -> [Jae] -> [JJ] -> None

    # node1 = Node('401n5')
    # print(node1.value)
    # node2 = Node('401n6', node1)
    # print(node2.value)
    # node2.next = None
    # node1.next = node2
# ['401n5'] -> ['401n6']
#     ll = LinkedList(node2)
#       node2       node1
# LL ['401n6'] ->  ['401n5'] -> None
# print(ll.head.value)
