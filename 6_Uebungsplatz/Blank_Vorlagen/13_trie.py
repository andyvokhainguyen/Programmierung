"""
Übung 13: Trie / Präfixbaum (WS2526-Stil)

Gegeben: Node, Trie-Gerüst, Testaufruf.
Selbst:  einfuegen, enthaelt, woerter_mit_praefix, _sammle_woerter.
"""


class Node:                                  # 🟩
    def __init__(self):
        self.kinder = {}
        self.ist_wortende = False


class Trie:                                  # 🟩 Gerüst vorgegeben
    def __init__(self):                      # 🟩
        self.wurzel = Node()

    def einfuegen(self, wort):
        # ✍️ SELBST: pro Buchstabe: fehlt Kind -> Node(); am Ende ist_wortende = True
        pass

    def enthaelt(self, wort):
        # ✍️ SELBST: Wort ablaufen; fehlt Buchstabe -> False; sonst ist_wortende zurück
        pass

    def woerter_mit_praefix(self, praefix):
        # ✍️ SELBST: zum Präfix-Knoten laufen (fehlt Buchstabe -> []),
        #            dann self._sammle_woerter(knoten, praefix, ergebnis)
        pass

    def _sammle_woerter(self, knoten, gebaut, ergebnis):
        # ✍️ SELBST: wenn knoten.ist_wortende -> gebaut anhängen;
        #            für ch in sorted(knoten.kinder): rekursiv mit gebaut+ch
        pass


# Testaufruf
trie = Trie()
for w in ["cat", "car", "cart", "dog", "dot", "dove"]:
    trie.einfuegen(w)
print(trie.woerter_mit_praefix("ca"))    # erwartet: ['car', 'cart', 'cat']
print(trie.woerter_mit_praefix("do"))    # erwartet: ['dog', 'dot', 'dove']
print(trie.enthaelt("car"), trie.enthaelt("care"))   # erwartet: True False
