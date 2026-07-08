"""
Übung 15: Zirkuläre verkettete Liste (WS2425-Stil)

Gegeben: Node, __init__.   Selbst: insert, delete, display.
Trick:   Abbruch bei != self.head (nicht != None) und Kreis wieder schließen.
"""


class Node:                                  # 🟩
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:                    # 🟩
    def __init__(self):                      # 🟩
        self.head = None

    def insert(self, key):
        # ✍️ SELBST: am Ende einfügen
        #   leer -> head = neuer; neuer.next = head (zeigt auf sich selbst)
        #   sonst: bis current.next == self.head laufen, anhängen, neuer.next = head
        pass

    def delete(self, key):
        # ✍️ SELBST:
        #   head-Fall (auch Sonderfall "nur 1 Element": head.next == head -> head = None)
        #   sonst mit current.next durchlaufen und Knoten überspringen
        pass

    def display(self):
        # ✍️ SELBST: while True: print(current.data); current = current.next;
        #            if current == self.head: break   (sonst Endlosschleife!)
        pass


# Testaufruf
cll = CircularLinkedList()
for x in ["A", "B", "C", "D"]:
    cll.insert(x)
cll.delete("B")
cll.display()                # erwartet: A C D
