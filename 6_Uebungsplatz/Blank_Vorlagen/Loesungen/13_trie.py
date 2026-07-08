"""
LÖSUNG 13: Trie / Präfixbaum
"""


class Node:
    def __init__(self):
        self.kinder = {}
        self.ist_wortende = False


class Trie:
    def __init__(self):
        self.wurzel = Node()

    def einfuegen(self, wort):               # 🟨 SELBST
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                aktueller.kinder[ch] = Node()
            aktueller = aktueller.kinder[ch]
        aktueller.ist_wortende = True

    def enthaelt(self, wort):                # 🟨 SELBST
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                return False
            aktueller = aktueller.kinder[ch]
        return aktueller.ist_wortende

    def woerter_mit_praefix(self, praefix):  # 🟨 SELBST
        aktueller = self.wurzel
        for ch in praefix:
            if ch not in aktueller.kinder:
                return []
            aktueller = aktueller.kinder[ch]
        ergebnis = []
        self._sammle_woerter(aktueller, praefix, ergebnis)
        return ergebnis

    def _sammle_woerter(self, knoten, gebaut, ergebnis):   # 🟨 SELBST
        if knoten.ist_wortende:
            ergebnis.append(gebaut)
        for ch in sorted(knoten.kinder.keys()):
            self._sammle_woerter(knoten.kinder[ch], gebaut + ch, ergebnis)


trie = Trie()
for w in ["cat", "car", "cart", "dog", "dot", "dove"]:
    trie.einfuegen(w)
print(trie.woerter_mit_praefix("ca"))    # ['car', 'cart', 'cat']
print(trie.woerter_mit_praefix("do"))    # ['dog', 'dot', 'dove']
print(trie.enthaelt("car"), trie.enthaelt("care"))   # True False
