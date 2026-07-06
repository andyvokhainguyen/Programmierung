"""
Aufgabe 4 - Klausur Programmierung WS2025/26
"""


class Node:
    def __init__(self):
        self.kinder = {}  # dict[str, Node]
        self.ist_wortende = False


class Trie:
    def __init__(self):
        self.wurzel = Node()

    def einfuegen(self, wort):
        """
        Fuegt ein Wort in den Trie ein.
        """
        pass

    def enthaelt(self, wort):
        """
        True, wenn wort vollstaendig enthalten ist (ist_wortende am Ende).
        """
        pass

    def woerter_mit_praefix(self, praefix):
        """
        Liefert alle Woerter, die mit praefix beginnen, alphabetisch sortiert.
        """
        pass

    def _sammle_woerter(self, knoten, gebaut, ergebnis):
        """
        Hilfsfunktion: sammelt ab knoten alle Woerter ein.
        gebaut ist das bisher aufgebaute Wort.
        """
        pass


trie = Trie()
woerter = ["cat", "car", "cart", "dog", "dot", "dove"]
for w in woerter:
    trie.einfuegen(w)

print(trie.woerter_mit_praefix("ca"))
print(trie.woerter_mit_praefix("do"))
print(trie.enthaelt("car"), trie.enthaelt("care"))
