"""
LÖSUNG 08: Einfach verkettete Liste (delete, insert_am_anfang)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):                  # 🟩 vorgegeben
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):                    # 🟩 vorgegeben
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):                  # 🟨 SELBST
        if self.head is None:
            return
        if self.head.data == data:           # Kopf-Sonderfall
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert_am_anfang(self, data):        # 🟨 SELBST
        neuer = Node(data)
        neuer.next = self.head               # alter Kopf hängt hinter dem neuen
        self.head = neuer                    # neuer ist jetzt der Kopf


liste = LinkedList()
for x in ["A", "B", "C", "D"]:
    liste.insert(x)              # hinten anhängen -> A B C D
liste.delete("B")                # -> A C D
liste.insert_am_anfang("X")      # vorne einfügen -> X A C D
liste.print_list()               # X A C D
