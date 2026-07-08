"""
Übung 08: Einfach verkettete Liste (SS23-Stil)

Gegeben: Node, __init__, insert, print_list.   Selbst: delete(data),
         insert_am_anfang(data).
"""


class Node:                                  # 🟩
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:                            # 🟩
    def __init__(self):                      # 🟩
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

    def delete(self, data):
        # ✍️ SELBST: Element mit Wert `data` entfernen
        #   1) Liste leer -> return
        #   2) Kopf-Sonderfall: self.head.data == data -> self.head = self.head.next
        #   3) sonst mit current.next durchlaufen und Knoten überspringen
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert_am_anfang(self, data):
        # ✍️ SELBST: neues Element VOR den Kopf setzen (wird neuer head)
        #   neuer = Node(data)
        #   neuer.next = self.head     # alter Kopf hängt hinter dem neuen
        #   self.head = neuer          # neuer ist jetzt der Kopf
        neuer = Node(data)
        neuer.next = self.head
        self.head = neuer


# Testaufruf
liste = LinkedList()
for x in ["A", "B", "C", "D"]:
    liste.insert(x)          # hinten anhängen -> A B C D
liste.delete("B")            # -> A C D
liste.insert_am_anfang("X")  # vorne einfügen -> X A C D
liste.print_list()           # erwartet: X A C D
