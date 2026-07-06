# Übungsklausur 3 – Programmierung (SS26)

**Hochschule Trier – Prof. Dr. Andreas Biesdorf**
Bearbeitungszeit: ca. 90 Minuten · Erreichbare Punkte: **90**
Hilfsmittel: nur Python-Syntax-Blatt (keine fertigen Implementierungen).

> Dritte Übungsklausur – bewusst **ohne Überschneidung** mit Probeklausur 1 und 2: **sys.argv** statt argparse/getopt, **Binärer Suchbaum** statt Queue/verketteter Liste, **Insertion-Sort (zwei Kriterien)** statt Bubble/Selection, neue Test- und Theoriethemen. Keine eigenständige Exception-Aufgabe.
> Versuche es zuerst selbst. Danach: Lösung in `Loesung.md` oder sag **„Lösung 3"**.

---

## Aufgabe 1 – Software Engineering (15 Punkte)

**a) (4 P)** Erklären Sie das **magische Dreieck des Projektmanagements** (welche drei Dimensionen?) und veranschaulichen Sie mit einem konkreten Beispiel, warum man nicht alle drei gleichzeitig optimieren kann.

**b) (4 P)** Nennen Sie die **Phasen der Softwareentwicklung** in der richtigen Reihenfolge (von der Analyse bis zum Betrieb). Geben Sie zu **drei** dieser Phasen jeweils die **Aufgabe** und das **Ergebnis (Artefakt)** an.

**c) (4 P)** Erklären Sie den Unterschied zwischen **funktionalen** und **nicht-funktionalen Anforderungen**. Geben Sie für ein **Online-Shop-System** je **zwei** Beispiele.

**d) (3 P)** Welcher **prozentuale Anteil** der Gesamtkosten entfällt typischerweise auf die **Betriebsphase**? Nennen Sie außerdem die **vier Wartungsarten**.

---

## Aufgabe 2 – Testen (20 Punkte)

**a) Black-Box (10 P)** — Gegeben ist folgende Funktion:
```python
def enthaelt_duplikate(liste):
    """ liste: eine Liste von Werten. Gibt True zurück, wenn mindestens
        ein Wert doppelt vorkommt, sonst False. """
    gesehen = []
    for element in liste:
        if element in gesehen:
            return True
        gesehen.append(element)
    return False
```
1. Bestimmen Sie sinnvolle, überschneidungsfreie **Äquivalenzklassen** (denken Sie an natürliche Partitionen und Randfälle wie die leere Liste).
2. Schreiben Sie zu jeder Klasse einen **pytest**-Test mit einem repräsentativen Wert.

**b) White-Box (10 P)** — Gegeben ist folgende Funktion:
```python
def maxOfDrei(a, b, c):
    """ a, b, c: Zahlen. Gibt das Maximum der drei Zahlen zurück. """
    if a > b:
        groesster = a
    else:
        groesster = b
    if c > groesster:
        groesster = c
    return groesster
```
1. Welche **Pfade** sollten für eine „path-complete" Prüfung getestet werden? Die Funktion enthält zwei aufeinanderfolgende Verzweigungen – benennen und begründen Sie die Kombinationen.
2. Schreiben Sie die zugehörigen **pytest**-Tests.

---

## Aufgabe 3 – Kommandozeile & Datei-IO mit **sys.argv** (20 Punkte)

Schreiben Sie ein Programm `caesar.py`, das eine Textdatei **zeilenweise** mit einer Caesar-Verschiebung ver- oder entschlüsselt und das Ergebnis in eine Ausgabedatei schreibt. Greifen Sie **direkt über `sys.argv`** auf die Argumente zu (nicht argparse/getopt).

Aufruf: `python3 caesar.py <infile> <outfile> <shift> <c|d>`
- `<infile>` : Eingabedatei · `<outfile>` : Ausgabedatei
- `<shift>` : ganze Zahl (Verschiebung) · `c` = chiffrieren, `d` = dechiffrieren

Bei falscher Argumentanzahl soll ein Hinweis auf den korrekten Aufruf ausgegeben werden.

**Hinweis:** Der Code für die Ver-/Entschlüsselung ist vorgegeben und muss nicht implementiert werden:
```python
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
```

---

## Aufgabe 4 – Datenstruktur: Binärer Suchbaum (20 Punkte)

Implementieren Sie einen **Binären Suchbaum** als Klasse `BinaryTree`, der ganze Zahlen verwaltet. Verwenden Sie eine Hilfsklasse `Node` mit `wert`, `left` und `right`.

Methoden:
- `insert(wert)` : fügt einen Wert gemäß der BST-Regel ein (kleiner → links, größer/gleich → rechts)
- `search(wert)` : gibt `True` zurück, wenn der Wert enthalten ist, sonst `False`
- `print_inorder()` : gibt die Werte per In-order-Traversierung aus

Demonstrieren Sie die Funktion mit einem Beispiel (mehrere Zahlen einfügen, `print_inorder`, eine Zahl suchen).

**Zusatzfrage (schriftlich):** Warum liefert die **In-order-Traversierung** eines binären Suchbaums die Werte in **aufsteigend sortierter** Reihenfolge? (1–2 Sätze)

---

## Aufgabe 5 – Sortierverfahren: Insertion-Sort (15 Punkte)

Gegeben ist eine Liste von Büchern als Dictionaries:
```python
buecher = [
    {"titel": "Python", "seiten": 300},
    {"titel": "Java",   "seiten": 300},
    {"titel": "C++",    "seiten": 250},
    {"titel": "Go",     "seiten": 400},
]
```

**a) (10 P)** Implementieren Sie eine Funktion `insertion_sort_buecher(buecher)`, die die Liste mit dem **Insertion-Sort-Algorithmus** sortiert: **primär aufsteigend nach `seiten`**, bei **gleicher Seitenzahl alphabetisch nach `titel`**. Geben Sie die sortierte Liste aus.

**b) (5 P)** Beantworten Sie schriftlich:
1. Wie lautet die Zeitkomplexität von Insertion-Sort im **besten** und im **schlechtesten** Fall?
2. Nennen Sie **einen Vorteil** von Insertion-Sort gegenüber Selection-Sort.

---

*Viel Erfolg!* — Lösung: `Loesung.md` oder sag **„Lösung 3"**.
