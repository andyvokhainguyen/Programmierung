"""
LÖSUNG 14: Ternärer Suchbaum (Einordnung nach Wortlänge)
"""


class Node:
    def __init__(self, wort):
        self.wort = wort
        self.links = None
        self.mitte = None
        self.rechts = None


class TernaererSuchbaum:
    def __init__(self):
        self.wurzel = None

    def einfuegen(self, wort):               # 🟩 Wrapper vorgegeben
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen_rekursiv(self.wurzel, wort)

    def _einfuegen_rekursiv(self, knoten, wort):   # 🟨 SELBST
        if len(wort) < len(knoten.wort):
            if knoten.links is None:
                knoten.links = Node(wort)
            else:
                self._einfuegen_rekursiv(knoten.links, wort)
        elif len(wort) == len(knoten.wort):
            if knoten.mitte is None:
                knoten.mitte = Node(wort)
            else:
                self._einfuegen_rekursiv(knoten.mitte, wort)
        else:
            if knoten.rechts is None:
                knoten.rechts = Node(wort)
            else:
                self._einfuegen_rekursiv(knoten.rechts, wort)

    def inorder_ausgabe(self):               # 🟩 Wrapper vorgegeben
        self._gesammelt = []
        self._inorder(self.wurzel)
        print(", ".join(self._gesammelt))

    def _inorder(self, knoten):              # 🟨 SELBST
        if knoten is not None:
            self._inorder(knoten.links)
            self._inorder(knoten.mitte)
            self._gesammelt.append(knoten.wort)
            self._inorder(knoten.rechts)


baum = TernaererSuchbaum()
for wort in ["Cat", "Hello", "Hi", "Dog", "World", "Python"]:
    baum.einfuegen(wort)
baum.inorder_ausgabe()       # Hi, Cat, Dog, Hello, World, Python
