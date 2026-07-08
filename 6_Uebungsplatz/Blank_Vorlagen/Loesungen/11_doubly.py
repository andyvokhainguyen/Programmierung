"""
LÖSUNG 11: Doppelt verkettete Liste
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None                     # 🟨 der Zusatz
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):                  # 🟨 SELBST
        neuer = Node(data)
        if self.head is None:
            self.head = neuer
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = neuer
        neuer.prev = current

    def print_vorwaerts(self):               # 🟨 SELBST
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def print_rueckwaerts(self):             # 🟨 SELBST
        current = self.head
        if current is None:
            return
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.data)
            current = current.prev


dll = DoublyLinkedList()
for x in ["A", "B", "C"]:
    dll.insert(x)
print("vorwaerts:")
dll.print_vorwaerts()        # A B C
print("rueckwaerts:")
dll.print_rueckwaerts()      # C B A
