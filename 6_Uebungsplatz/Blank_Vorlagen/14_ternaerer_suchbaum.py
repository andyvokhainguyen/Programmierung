"""
Übung 14: Ternärer Suchbaum (SS25-Stil), Einordnung nach Wortlänge

Gegeben: Node, einfuegen-Wrapper, inorder_ausgabe-Wrapper, Testaufruf.
Selbst:  _einfuegen_rekursiv, _inorder.
"""


class Node:                                  # 🟩
    def __init__(self, wort):
        self.wort = wort
        self.links = None
        self.mitte = None
        self.rechts = None


class TernaererSuchbaum:                     # 🟩
    def __init__(self):                      # 🟩
        self.wurzel = None

    def einfuegen(self, wort):               # 🟩 Wrapper vorgegeben
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen_rekursiv(self.wurzel, wort)

    def _einfuegen_rekursiv(self, knoten, wort):
        # ✍️ SELBST: nach LÄNGE einordnen
        #   len(wort) < len(knoten.wort) -> links
        #   ==                            -> mitte
        #   >                             -> rechts
        #   Platz None -> Node(wort), sonst rekursiv weiter
        pass

    def inorder_ausgabe(self):               # 🟩 Wrapper vorgegeben
        self._gesammelt = []
        self._inorder(self.wurzel)
        print(", ".join(self._gesammelt))

    def _inorder(self, knoten):
        # ✍️ SELBST: links -> mitte -> knoten.wort anhängen -> rechts
        if knoten is not None:
            pass


# Testaufruf
baum = TernaererSuchbaum()
for wort in ["Cat", "Hello", "Hi", "Dog", "World", "Python"]:
    baum.einfuegen(wort)
baum.inorder_ausgabe()       # erwartet (nach Länge): Hi, Cat, Dog, Hello, World, Python
