# Lösungsschlüssel – Übungsklausur 4 (SS26)

Gesamt: **90 Punkte**. Lösungen zu [Aufgaben.md](Aufgaben.md).

---

## Aufgabe 1 – Software Engineering (15 P)

**a) Versteckte Anforderungen (4 P):**
- **Was:** Anforderungen, die der Kunde **nicht explizit nennt**, die sich aber aus dem Kontext ergeben und trotzdem erfüllt werden müssen.
- **Erkennen:** durch gezieltes **Nachfragen / Analyse** des Einsatzkontexts.
- Beispiele (zwei genügen): Einsatzort → **Wartungsart** (Remote-Zugang nötig) · Benutzungsfrequenz → **Performanz** (1000 gleichzeitige Nutzer) · Ausfallfolgen → **Robustheit** · Anwenderprofil → **Internationalisierung** · Geschäftsplanung → **Erweiterbarkeit**.

**b) Brooks'sches Gesetz (4 P):**
- Sinngemäß: **„Adding manpower to a late software project makes it later."** – Mehr Personal auf einem verspäteten Projekt macht es noch später.
- Begründung über den **Kommunikationsaufwand:** Die Zahl der Kommunikationskanäle wächst mit **n·(n-1)/2** (5 Personen = 10 Kanäle, 50 Personen = 1225!). Dazu kommen **Einarbeitungszeit** (Neue binden erfahrene Kollegen) und die Tatsache, dass **nicht alle Aufgaben parallelisierbar** sind.

**c) Testpyramide (4 P):**
- Teststufen von unten nach oben: **Unit-Tests → Integrationstests → System-/E2E-Tests** (Regressionstests laufen begleitend).
- Grundidee: **viele schnelle Unit-Tests** an der breiten Basis, **wenige aufwändige** E2E-Tests an der Spitze.

**d) 1-10-100-Regel (3 P):**
Die Kosten der Fehlerbehebung **steigen drastisch**, je später ein Fehler entdeckt wird: Fehler in der **Anforderungsanalyse** kosten ~1×, in der Implementierung ~10×, **nach Auslieferung 100–1000×**. → Sorgfalt in frühen Phasen zahlt sich massiv aus.

---

## Aufgabe 2 – Testen (20 P)

**a) Black-Box `ist_palindrom` (10 P)**

| Klasse | Eingabe | Erwartung |
|---|---|---|
| K1 leerer String (Randfall) | `""` | True |
| K2 ein Zeichen (Randfall) | `"a"` | True |
| K3 Palindrom, gerade Länge | `"anna"` | True |
| K4 Palindrom, ungerade Länge | `"aha"` | True |
| K5 kein Palindrom | `"haus"` | False |

Begründung: leerer String und ein Zeichen sind Randfälle (immer Palindrom); Palindrome mit gerader/ungerader Länge und ein Nicht-Palindrom decken die inhaltlichen Fälle ab.

```python
from src import aufgabe02

def test_palindrom_leer():
    assert aufgabe02.ist_palindrom("") is True

def test_palindrom_ein_zeichen():
    assert aufgabe02.ist_palindrom("a") is True

def test_palindrom_gerade():
    assert aufgabe02.ist_palindrom("anna") is True

def test_palindrom_ungerade():
    assert aufgabe02.ist_palindrom("aha") is True

def test_kein_palindrom():
    assert aufgabe02.ist_palindrom("haus") is False
```

**b) White-Box `zaehle_grosse_zahlen` (10 P)**

Schleife 0 / mehrfach durchlaufen + beide `if`-Ausgänge:
| Pfad | Fall | Beispiel | Erwartung |
|---|---|---|---|
| P1 | Schleife 0× (leere Liste) | `zaehle_grosse_zahlen([], 5)` | 0 |
| P2 | Schleife läuft, `if` immer False | `zaehle_grosse_zahlen([1, 2], 5)` | 0 |
| P3 | Schleife läuft, `if` immer True | `zaehle_grosse_zahlen([7, 9], 5)` | 2 |
| P4 | gemischt (True und False) | `zaehle_grosse_zahlen([3, 7, 2, 9], 5)` | 2 |

```python
def test_grosse_leer():
    assert aufgabe02.zaehle_grosse_zahlen([], 5) == 0

def test_grosse_keine_ueber_grenze():
    assert aufgabe02.zaehle_grosse_zahlen([1, 2], 5) == 0

def test_grosse_alle_ueber_grenze():
    assert aufgabe02.zaehle_grosse_zahlen([7, 9], 5) == 2

def test_grosse_gemischt():
    assert aufgabe02.zaehle_grosse_zahlen([3, 7, 2, 9], 5) == 2
```

---

## Aufgabe 3 – `textanalyse.py` (argparse) (20 P)

```python
import argparse


def analysiere(pfad, befehl):
    with open(pfad, "r", encoding="utf-8") as datei:
        inhalt = datei.read()

    woerter = inhalt.split()

    if befehl == "woerter":
        return len(woerter)
    elif befehl == "zeichen":
        return len(inhalt)
    elif befehl == "haeufigstes":
        haeufigkeit = {}
        for wort in woerter:
            haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1
        return max(haeufigkeit, key=haeufigkeit.get)


def main():
    parser = argparse.ArgumentParser(description="Textanalyse-Tool.")
    parser.add_argument("--input", "-i", required=True, help="Eingabedatei")
    parser.add_argument("--output", "-o", required=True, help="Ausgabedatei")
    parser.add_argument("--befehl", "-b", required=True,
                        choices=["woerter", "zeichen", "haeufigstes"])
    args = parser.parse_args()

    ergebnis = analysiere(args.input, args.befehl)
    with open(args.output, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {args.befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")


if __name__ == "__main__":
    main()
```
Für `Das ist ein Test. Dieser Test ist nur ein Beispiel.`:
`woerter` → 10 · `haeufigstes` → `ist` (bzw. das zuerst eingefügte häufigste Wort).

---

## Aufgabe 4 – Stack + Klammerprüfung (20 P)

**a) Stack (12 P)**
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()          # letztes Element (LIFO)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
```

**b) Klammerprüfung mit dem Stack (8 P)**
```python
def ist_ausgeglichen(ausdruck):
    stack = Stack()
    paare = {")": "(", "]": "[", "}": "{"}      # schließend -> passend öffnend
    for zeichen in ausdruck:
        if zeichen in "([{":
            stack.push(zeichen)                 # Öffnungsklammer merken
        elif zeichen in paare:                  # Schließklammer
            if stack.is_empty() or stack.pop() != paare[zeichen]:
                return False
    return stack.is_empty()                     # alle geöffneten wieder geschlossen?


print(ist_ausgeglichen("{[()]}"))     # True
print(ist_ausgeglichen("{[(])}"))     # False
print(ist_ausgeglichen("(a+b)*[c]"))  # True
```
**Warum Stack?** Die zuletzt geöffnete Klammer muss zuerst geschlossen werden = **LIFO**.

---

## Aufgabe 5 – Quicksort (15 P)

**a) (10 P)**
```python
def quicksort(zahlen):
    # Basisfall: 0 oder 1 Element ist bereits sortiert
    if len(zahlen) <= 1:
        return zahlen

    pivot = zahlen[0]
    # '<=' behält Duplikate (sonst gingen gleiche Werte verloren)
    kleiner = [x for x in zahlen[1:] if x <= pivot]
    groesser = [x for x in zahlen[1:] if x > pivot]

    return quicksort(kleiner) + [pivot] + quicksort(groesser)


print(quicksort([5, 2, 8, 1, 9, 3, 5]))
# [1, 2, 3, 5, 5, 8, 9]   (beide 5er bleiben erhalten)
```

**b) (5 P)**
1. Quicksort: **mittlerer Fall O(n·log n)**, **schlechtester Fall O(n²)**.
2. Der schlechteste Fall tritt bei **ungünstiger Pivotwahl** ein – z.B. wenn die Liste (bei Pivot = erstes Element) bereits **sortiert** oder umgekehrt sortiert ist, sodass eine Teilliste immer leer bleibt und die Rekursionstiefe auf n anwächst.

---

## Punkteverteilung
| Aufgabe | Thema | Punkte |
|---|---|---|
| 1 | Software Engineering | 15 |
| 2 | Testen (Black-/White-Box + pytest) | 20 |
| 3 | Kommandozeile & Datei-IO (argparse) | 20 |
| 4 | Stack + Klammerprüfung | 20 |
| 5 | Quicksort | 15 |
| **Summe** | | **90** |
