# 🧱 Grundgerüste zu allem (das Minimum zum Auswendiglernen)

Pro Themenfamilie **ein** Skelett. Wenn du diese ~8 Gerüste blank schreiben kannst, deckst du jede Altklausur-Aufgabe ab – du änderst pro Aufgabe nur die markierte Stelle (**▶ hier anpassen**).

**Inhalt:** 1) Testen · 2) getopt · 3) Datei-IO · 4) Verkettete Liste · 5) Stack/Queue · 6) Baum · 7) Sortier-Gerüste · 8) „nur die Vergleichszeile"

---

## 1) Testen – pytest-Gerüst
```python
from src import aufgabe02          # zu testende Datei liegt in src/
import pytest

def test_normalfall():            # Name MUSS mit test_ beginnen
    assert aufgabe02.funktion(80) == 1        # ▶ Eingabe/Erwartung anpassen

def test_grenzwert():
    assert aufgabe02.funktion(50) == 4        # ▶ genau AUF der Grenze

def test_exception():
    with pytest.raises(ValueError):           # ▶ erwarteter Fehlertyp
        aufgabe02.funktion(-1)
```
**Testfälle finden:** if/elif → je Kategorie 1 Wert **+ Grenzwert** · Liste → leer/1/mehrere · Schleife → 0×/1×/mehrfach · Rekursion → Basisfall/1×/mehrfach.

---

## 2) Kommandozeile – getopt-Gerüst (das universelle)
```python
import sys
import getopt

def main(argv):
    inputfile = ""
    outputfile = ""
    befehl = ""
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",              # ▶ Buchstabe + ':' = braucht Wert
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError:
        print("prog.py -i <in> -o <out> -b <befehl>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("prog.py -i <in> -o <out> -b <befehl>")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-b", "--befehl"):
            befehl = arg

    if inputfile == "" or outputfile == "" or befehl == "":       # Pflicht selbst prüfen
        print("Fehler: -i, -o und -b sind erforderlich.")
        sys.exit(2)

    # ▶ hier: Datei einlesen, verarbeiten, Ergebnis schreiben

if __name__ == "__main__":
    main(sys.argv[1:])
```

---

## 3) Datei-IO – lesen & schreiben
```python
# Lesen (zeilenweise)
with open("log.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:
        if zeile.strip() == "":
            continue
        teile = zeile.strip().split(";")      # ▶ Trennzeichen je nach Format
        # ... verarbeiten ...

# Schreiben ("w"=neu/überschreiben, "a"=anhängen)
with open("ergebnis.txt", "w", encoding="utf-8") as datei:
    datei.write("Text\n")                     # \n selbst setzen
```

---

## 4) Datenstruktur – Verkettete Liste
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None                      # ▶ doppelt verkettet: + self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):                   # am Ende anhängen
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:               # ▶ zirkulär: while current.next != self.head
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:                        # ▶ zirkulär: while True + break bei head
            print(current.data)
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:            # Kopf-Sonderfall
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next   # Knoten überspringen
                return
            current = current.next
```

---

## 5) Datenstruktur – Stack & Queue (fast identisch)
```python
class Stack:                          # LIFO – hinten
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()       # ▶ Queue: self.queue.pop(0)  (vorne!)
    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]         # ▶ Queue: self.queue[0]
    def is_empty(self):
        return len(self.stack) == 0
    def display(self):
        print(self.stack)
```
**Queue** = dasselbe mit `enqueue`/`append` und `dequeue`/`pop(0)`. **Einziger Unterschied: hinten (Stack) vs. vorne (Queue).**

---

## 6) Datenstruktur – Baum (Grundgerüst, hier BST)
```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None                     # ▶ ternär: + self.mitte  |  Trie: self.kinder = {}
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):                   # Wrapper (oft vorgegeben)
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:                  # ▶ Einordnungskriterium
            if node.left is None:             #   TST: len(wort) < len(knoten.wort)
                node.left = Node(data)        #   Trie: pro Buchstabe ins dict
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):              # In-order = sortierte Ausgabe
        if node is not None:
            self._print_tree(node.left)       # links
            print(node.data)                  # ich   ▶ ternär: dazwischen self.mitte besuchen
            self._print_tree(node.right)      # rechts
```

---

## 7) Sortierverfahren – die Gerüste

```python
# --- Bubble ---
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:               # ▶ Vergleichszeile
                a[j], a[j + 1] = a[j + 1], a[j]

# --- Selection ---
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:               # ▶ Vergleichszeile
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]

# --- Insertion ---
def insertion_sort(a):
    for i in range(1, len(a)):
        pivot = a[i]
        j = i - 1
        while j >= 0 and a[j] > pivot:        # ▶ Vergleichszeile
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = pivot

# --- Quicksort ---
def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    kleiner  = [x for x in a[1:] if x <= pivot]   # ▶ Vergleich (<= behält Duplikate)
    groesser = [x for x in a[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)

# --- Mergesort (merge ist in der Klausur oft vorgegeben) ---
def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(mergesort(a[:mid]), mergesort(a[mid:]))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:                # ▶ Vergleichszeile
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Heapsort (heapify ist in der Klausur oft vorgegeben) ---
def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):       # 1) Max-Heap bauen
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):             # 2) größtes ans Ende, Heap verkleinern
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]:     # ▶ Vergleich
        largest = left
    if right < n and a[right] > a[largest]:   # ▶ Vergleich
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)
```

---

## 8) 🔑 Die eine Stelle, die sich ändert (Vergleichszeile)
Alle Sortierer haben dasselbe Gerüst – nur **eine Zeile** entscheidet über das Kriterium:

| Aufgabe | Vergleich (statt `a > b`) |
|---|---|
| Zahlen aufsteigend | `a > b` |
| Strings nach Länge | `len(a) > len(b)` |
| Länge, dann alphabetisch | `(len(a), a) > (len(b), b)` |
| Dict/Objekt nach Feld | `a["gehalt"] > b["gehalt"]` |
| absteigend | `>` ↔ `<` tauschen |

**Das ist der ganze Trick:** Gerüst sitzt → pro Aufgabe nur die ▶-Stelle anpassen.

---

### So nutzt du diese Datei
1. Erst **verstehen**, dann jedes Gerüst **blank** aus dem Kopf schreiben (in `6_Uebungsplatz/Blank_Vorlagen/`).
2. Danach die Varianten üben, indem du nur die **▶-Stelle** änderst (z. B. Sortieren nach Länge, Baum nach Wortlänge).
3. Volle, klausurgetreue Fassungen: [`9_Altklausuren_Loesungen_komplett.md`](9_Altklausuren_Loesungen_komplett.md); Vorgabe-vs-Selbst: [`7_Codes_Vorgabe_vs_Selbst.md`](7_Codes_Vorgabe_vs_Selbst.md).
