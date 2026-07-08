"""
LÖSUNG 15: Zirkuläre verkettete Liste
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):                   # 🟨 SELBST
        neuer = Node(key)
        if self.head is None:
            self.head = neuer
            neuer.next = self.head           # zeigt auf sich selbst
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = neuer
            neuer.next = self.head           # Kreis schließen

    def delete(self, key):                   # 🟨 SELBST
        if self.head is None:
            return
        if self.head.data == key:
            if self.head.next == self.head:  # nur ein Element
                self.head = None
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return
        current = self.head
        while current.next != self.head:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def display(self):                       # 🟨 SELBST
        if self.head is None:
            print("Liste ist leer")
            return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break


cll = CircularLinkedList()
for x in ["A", "B", "C", "D"]:
    cll.insert(x)
cll.delete("B")
cll.display()                # A C D
