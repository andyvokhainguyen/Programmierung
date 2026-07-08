"""
Übung 10: Binärer Suchbaum (SS24-Stil, + delete aus Skript 05)

Gegeben: Node, __init__, insert-Wrapper.
Selbst:  _insert, print_tree (+ _print_tree), search, delete.
"""


class Node:                                  # 🟩
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:                            # 🟩
    def __init__(self):                      # 🟩
        self.root = None

    def insert(self, data):                  # 🟩 Wrapper vorgegeben
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # ✍️ SELBST: rekursiv - data < node.data -> links, sonst rechts;
        #            Platz None -> Node(data), sonst rekursiv weiter
        pass

    def print_tree(self):
        # ✍️ SELBST: Wrapper -> self._print_tree(self.root), falls root vorhanden
        pass

    def _print_tree(self, node):
        # ✍️ SELBST: In-order: links -> print(node.data) -> rechts (= sortiert)
        pass

    def search(self, data):
        # ✍️ SELBST: True/False - rekursiv links/rechts absteigen
        pass

    def delete(self, data):
        # ✍️ SELBST (schwieriger, aus Skript): self.root = self._delete(self.root, data)
        pass

    def _delete(self, node, data):
        # ✍️ SELBST: 3 Fälle - Blatt / ein Kind / zwei Kinder (kleinsten rechts holen)
        pass


# Testaufruf
bst = BinaryTree()
for x in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(x)
bst.print_tree()             # erwartet: 5 10 15 20 25 30 35 (aufsteigend)
