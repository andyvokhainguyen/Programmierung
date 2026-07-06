# Lösungsschlüssel – Übungsklausur 3 (SS26)

Gesamt: **90 Punkte**. Lösungen zu [Aufgaben.md](Aufgaben.md).

---

## Aufgabe 1 – Software Engineering (15 P)

**a) Magisches Dreieck (4 P):**
- Drei konkurrierende Dimensionen: **ZEIT – KOSTEN – QUALITÄT**.
- Die Änderung einer Dimension wirkt sich **zwangsläufig** auf die anderen aus; man kann nicht alle drei gleichzeitig optimieren.
- Beispiel: Ein Projekt soll **früher** fertig werden (Zeit ↓). Folge: entweder **mehr Personal** einstellen (Kosten ↑) oder **Funktionen/Tests weglassen** (Qualität ↓).

**b) Phasen der Softwareentwicklung (4 P):**
Reihenfolge: **Analyse → Definition → Architektur → Design → Implementierung → (Modultest →) Integration/Test → Abnahme → Einführung/Betrieb.**
Beispiele für Aufgabe + Ergebnis (drei genügen):
| Phase | Aufgabe | Ergebnis (Artefakt) |
|---|---|---|
| Analyse | verstehen, was der Kunde will; Ist-Ablauf aufnehmen | Anforderungsdokumentation |
| Definition | festlegen, *was* das System tun soll | Spezifikation + Abnahmekriterien |
| Implementierung | Feinentwurf in Code umsetzen | Code + Unit Tests |
| Abnahme | Gesamtsystem gegen Anforderungen prüfen | Abnahmeprotokoll |

**c) Funktionale vs. nicht-funktionale Anforderungen (4 P):**
- **Funktional = WAS** das System tun soll (konkrete Funktionen).
- **Nicht-funktional = WIE GUT** (Qualitätseigenschaften).
- Online-Shop, je 2 Beispiele:
  - **Funktional:** Produkte in den Warenkorb legen; Bezahlvorgang durchführen. *(auch: Produktsuche, Bestellhistorie)*
  - **Nicht-funktional:** Seitenladezeit < 2 s (Effizienz); Verschlüsselung der Zahlungsdaten (Sicherheit). *(auch: Verfügbarkeit, Skalierbarkeit)*

**d) Betriebsphase (3 P):**
- **~80 %** der Gesamtkosten entfallen auf den Betrieb.
- Vier **Wartungsarten:** **korrektiv** (Fehlerbehebung), **adaptiv** (Anpassung an veränderte Rahmenbedingungen), **perfektiv** (Verbesserung bestehender Funktionen), **präventiv** (Verbesserung der Wartbarkeit).

---

## Aufgabe 2 – Testen (20 P)

**a) Black-Box `enthaelt_duplikate` (10 P)**

Natürliche Partitionen + Randfälle:
| Klasse | Eingabe | Erwartung |
|---|---|---|
| K1 leere Liste (Randfall) | `[]` | False |
| K2 ein Element | `[5]` | False |
| K3 mehrere, keine Duplikate | `[1, 2, 3]` | False |
| K4 mit Duplikaten | `[1, 2, 2]` | True |
| K5 alle gleich (Randfall) | `[7, 7, 7]` | True |

Begründung: leere vs. einelementige vs. mehrelementige Liste; mit vs. ohne Duplikate; K5 prüft den Extremfall, dass alle Elemente identisch sind.

```python
from src import aufgabe02

def test_dupl_leer():
    assert aufgabe02.enthaelt_duplikate([]) is False

def test_dupl_ein_element():
    assert aufgabe02.enthaelt_duplikate([5]) is False

def test_dupl_keine():
    assert aufgabe02.enthaelt_duplikate([1, 2, 3]) is False

def test_dupl_mit():
    assert aufgabe02.enthaelt_duplikate([1, 2, 2]) is True

def test_dupl_alle_gleich():
    assert aufgabe02.enthaelt_duplikate([7, 7, 7]) is True
```

**b) White-Box `maxOfDrei` (10 P)**

Zwei aufeinanderfolgende Verzweigungen → 4 Pfadkombinationen:
| Pfad | `a > b` | `c > groesster` | Ergebnis | Beispiel |
|---|---|---|---|---|
| P1 | True | True | c ist Maximum | maxOfDrei(3, 1, 5) → 5 |
| P2 | True | False | a ist Maximum | maxOfDrei(5, 1, 3) → 5 |
| P3 | False | True | c ist Maximum | maxOfDrei(1, 3, 5) → 5 |
| P4 | False | False | b ist Maximum | maxOfDrei(1, 5, 3) → 5 |

```python
def test_max_p1():
    assert aufgabe02.maxOfDrei(3, 1, 5) == 5

def test_max_p2():
    assert aufgabe02.maxOfDrei(5, 1, 3) == 5

def test_max_p3():
    assert aufgabe02.maxOfDrei(1, 3, 5) == 5

def test_max_p4():
    assert aufgabe02.maxOfDrei(1, 5, 3) == 5
```

---

## Aufgabe 3 – `caesar.py` mit sys.argv (20 P)

```python
import sys


# --- vorgegeben ---
def caesar_chiffrieren(text, verschiebung):
    ergebnis = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            ergebnis += chr((ord(char) - offset + verschiebung) % 26 + offset)
        else:
            ergebnis += char
    return ergebnis


def caesar_dechiffrieren(text, verschiebung):
    return caesar_chiffrieren(text, -verschiebung)
# --- /vorgegeben ---


# genau 4 Argumente erforderlich (+ Skriptname = 5)
if len(sys.argv) != 5:
    print("Aufruf: python3 caesar.py <infile> <outfile> <shift> <c|d>")
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]
shift = int(sys.argv[3])
modus = sys.argv[4]

with open(infile, "r", encoding="utf-8") as ein, \
     open(outfile, "w", encoding="utf-8") as aus:
    for zeile in ein:
        if modus == "c":
            aus.write(caesar_chiffrieren(zeile, shift))
        elif modus == "d":
            aus.write(caesar_dechiffrieren(zeile, shift))
        else:
            print("Modus muss 'c' oder 'd' sein.")
            sys.exit()
```
Kontrolle: `python3 caesar.py klartext.txt geheim.txt 3 c` verschlüsselt; `python3 caesar.py geheim.txt zurueck.txt 3 d` liefert den Klartext wieder.

---

## Aufgabe 4 – Binärer Suchbaum (20 P)

```python
class Node:
    def __init__(self, wert):
        self.wert = wert
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, wert):
        if self.root is None:
            self.root = Node(wert)
        else:
            self._insert(self.root, wert)

    def _insert(self, node, wert):
        if wert < node.wert:                 # kleiner -> links
            if node.left is None:
                node.left = Node(wert)
            else:
                self._insert(node.left, wert)
        else:                                # größer/gleich -> rechts
            if node.right is None:
                node.right = Node(wert)
            else:
                self._insert(node.right, wert)

    def search(self, wert):
        return self._search(self.root, wert)

    def _search(self, node, wert):
        if node is None:
            return False
        if wert == node.wert:
            return True
        elif wert < node.wert:
            return self._search(node.left, wert)
        else:
            return self._search(node.right, wert)

    # In-order: links -> Knoten -> rechts  => aufsteigend sortiert
    def print_inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.wert)
            self._inorder(node.right)


# Anwendungsbeispiel
bt = BinaryTree()
for zahl in [20, 10, 30, 5, 15, 25]:
    bt.insert(zahl)
bt.print_inorder()          # 5 10 15 20 25 30
print(bt.search(15))        # True
print(bt.search(99))        # False
```

**Zusatzfrage:** Bei der In-order-Traversierung wird für jeden Knoten **zuerst der linke Teilbaum** (nur kleinere Werte), **dann der Knoten selbst**, **dann der rechte Teilbaum** (nur größere Werte) besucht. Da diese Ordnung rekursiv für jeden Knoten gilt, werden die Werte automatisch in **aufsteigender Reihenfolge** ausgegeben.

---

## Aufgabe 5 – Insertion-Sort mit zwei Kriterien (15 P)

**a) (10 P)**
```python
def insertion_sort_buecher(buecher):
    n = len(buecher)
    for i in range(1, n):
        pivot = buecher[i]
        j = i - 1
        # Vergleich über den Schlüssel (seiten, titel): primär Seiten, sekundär Titel
        while j >= 0 and (buecher[j]["seiten"], buecher[j]["titel"]) \
                       > (pivot["seiten"], pivot["titel"]):
            buecher[j + 1] = buecher[j]
            j -= 1
        buecher[j + 1] = pivot
    return buecher


buecher = [
    {"titel": "Python", "seiten": 300},
    {"titel": "Java",   "seiten": 300},
    {"titel": "C++",    "seiten": 250},
    {"titel": "Go",     "seiten": 400},
]
for b in insertion_sort_buecher(buecher):
    print(b)
# C++ (250) | Java (300) | Python (300) | Go (400)
#   -> bei 300 Seiten steht "Java" vor "Python" (alphabetisch)
```

**b) (5 P)**
1. Insertion-Sort: **bester Fall O(n)** (Liste bereits sortiert – die while-Schleife bricht sofort ab), **schlechtester Fall O(n²)** (umgekehrt sortiert).
2. Vorteil gegenüber Selection-Sort (einer genügt):
   - Insertion-Sort ist **adaptiv**: bei (fast) sortierten Daten nur **O(n)**; Selection-Sort ist **immer O(n²)**.
   - Insertion-Sort ist **stabil**, Selection-Sort nicht.

---

## Punkteverteilung
| Aufgabe | Thema | Punkte |
|---|---|---|
| 1 | Software Engineering | 15 |
| 2 | Testen (Black-/White-Box + pytest) | 20 |
| 3 | Kommandozeile & Datei-IO (sys.argv) | 20 |
| 4 | Binärer Suchbaum | 20 |
| 5 | Insertion-Sort (zwei Kriterien) | 15 |
| **Summe** | | **90** |
