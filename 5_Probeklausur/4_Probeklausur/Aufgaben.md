# Übungsklausur 4 – Programmierung (SS26)

**Hochschule Trier – Prof. Dr. Andreas Biesdorf**
Bearbeitungszeit: ca. 90 Minuten · Erreichbare Punkte: **90**
Hilfsmittel: nur Python-Syntax-Blatt (keine fertigen Implementierungen).

> Vierte Übungsklausur – ohne Überschneidung mit Probeklausur 1–3: **Quicksort** (Divide-and-Conquer), **Stack** + Klammerprüfung, **for-Schleifen-White-Box**, String-Black-Box und neue Theoriethemen. Keine eigenständige Exception-Aufgabe.
> Versuche es zuerst selbst. Danach: Lösung in `Loesung.md` oder sag **„Lösung 4"**.

---

## Aufgabe 1 – Software Engineering (15 Punkte)

**a) (4 P)** Was sind **versteckte Anforderungen**? Wie kann man sie erkennen? Geben Sie **zwei** Beispiele (jeweils: welche Information deutet auf welche Anforderung hin).

**b) (4 P)** Nennen Sie das **Brooks'sche Gesetz** (sinngemäß) und erklären Sie anhand des **Kommunikationsaufwands**, warum es gilt.

**c) (4 P)** Nennen Sie die **Teststufen** der **Testpyramide** (von unten nach oben) und beschreiben Sie die **Grundidee** der Pyramide in einem Satz.

**d) (3 P)** Erklären Sie die **1-10-100-Regel** der Fehlerkosten.

---

## Aufgabe 2 – Testen (20 Punkte)

**a) Black-Box (10 P)** — Gegeben ist folgende Funktion:
```python
def ist_palindrom(text):
    """ text: ein String (nur Kleinbuchstaben). Gibt True zurück, wenn text
        vorwärts wie rückwärts gelesen gleich ist, sonst False. """
    return text == text[::-1]
```
1. Bestimmen Sie sinnvolle, überschneidungsfreie **Äquivalenzklassen** (denken Sie an Randfälle wie leerer String / ein Zeichen).
2. Schreiben Sie zu jeder Klasse einen **pytest**-Test.

**b) White-Box (10 P)** — Gegeben ist folgende Funktion mit einer **for-Schleife**:
```python
def zaehle_grosse_zahlen(liste, grenze):
    """ liste: Liste von Zahlen, grenze: Zahl. Gibt die Anzahl der
        Elemente zurück, die größer als grenze sind. """
    anzahl = 0
    for zahl in liste:
        if zahl > grenze:
            anzahl += 1
    return anzahl
```
1. Welche **Pfade** sollten geprüft werden? Berücksichtigen Sie die Schleife (0 / 1 / mehrfach durchlaufen) **und** beide Ausgänge der `if`-Bedingung.
2. Schreiben Sie die zugehörigen **pytest**-Tests.

---

## Aufgabe 3 – Kommandozeile & Datei-IO (20 Punkte)

Schreiben Sie ein Programm `textanalyse.py`, das eine Textdatei einliest und je nach Befehl auswertet. Verwenden Sie das **argparse**-Modul.

Unterstützte Argumente:
- `--input` / `-i` : Eingabedatei (Pflicht)
- `--output` / `-o` : Ausgabedatei (Pflicht)
- `--befehl` / `-b` : einer von `woerter`, `zeichen`, `haeufigstes` (Pflicht)

Bedeutung:
- `woerter` : Anzahl der Wörter in der Datei
- `zeichen` : Anzahl der Zeichen in der Datei
- `haeufigstes` : das **am häufigsten vorkommende Wort**

Das Ergebnis wird in die Ausgabedatei geschrieben, z.B.:
```
Befehl: haeufigstes
Ergebnis: ist
```
Beispielaufruf: `python3 textanalyse.py -i text.txt -o ergebnis.txt -b woerter`

---

## Aufgabe 4 – Datenstruktur: Stack + Anwendung (20 Punkte)

**a) (12 P)** Implementieren Sie einen **Stack** (LIFO) als Klasse `Stack` mit den Methoden:
- `push(item)` : Element oben auflegen
- `pop()` : oberstes Element entfernen und zurückgeben (bei leer `None`)
- `peek()` : oberstes Element ansehen, ohne es zu entfernen (bei leer `None`)
- `is_empty()` : `True`, wenn leer
- `size()` : Anzahl der Elemente

**b) (8 P)** Schreiben Sie eine Funktion `ist_ausgeglichen(ausdruck)`, die mithilfe Ihres **Stacks** prüft, ob die Klammern in einem String korrekt gesetzt sind (Klammertypen `()`, `[]`, `{}`). Rückgabe `True`/`False`.
Beispiele: `"{[()]}"` → `True` · `"{[(])}"` → `False` · `"(a+b)*[c]"` → `True`.

---

## Aufgabe 5 – Sortierverfahren: Quicksort (15 Punkte)

**a) (10 P)** Implementieren Sie eine Funktion `quicksort(zahlen)`, die eine Liste von Zahlen mit dem **Quicksort-Algorithmus** aufsteigend sortiert (Divide-and-Conquer). Wählen Sie als Pivot das erste Element. Achten Sie darauf, dass **Duplikate erhalten** bleiben. Testen Sie mit `[5, 2, 8, 1, 9, 3, 5]`.

**b) (5 P)** Beantworten Sie schriftlich:
1. Wie lautet die Zeitkomplexität von Quicksort im **mittleren** und im **schlechtesten** Fall?
2. Wann tritt der schlechteste Fall ein?

---

*Viel Erfolg!* — Lösung: `Loesung.md` oder sag **„Lösung 4"**.
