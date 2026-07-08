# 🔍 Lückenanalyse – Was kam dran, was (noch) nie?

Vergleich **aller 6 Altklausuren** (SS23 → WS2526). Ziel: erkennen, welche Themen der Prof **wiederholt**, welche er **noch nie** abgefragt hat – und daraus ableiten, was in der nächsten Klausur wahrscheinlich ist.

> Grundregel des Profs: **Im Normalfall wird nichts ein zweites Mal identisch abgefragt.** Das *Aufgabenmuster* bleibt aber gleich – nur die konkrete Datenstruktur / das Sortierverfahren wechselt.

---

## 1) Das feste Klausur-Skelett (immer gleich)

Jede Klausur besteht aus **denselben Bausteinen**, nur unterschiedlich verpackt:

| Block | Thema | kommt vor |
|---|---|---|
| A | **SE-Theorie** (Software Engineering) | in **jeder** Klausur |
| B | **Testen** (Black-Box / White-Box / pytest) | in **jeder** Klausur |
| C | **Kommandozeile + Datei-I/O** (getopt/argparse, `with open`) | in **jeder** Klausur |
| D | **Datenstruktur** als Klasse | in **jeder** Klausur |
| E | **Sortierverfahren** | in **jeder** Klausur |
| (F) | **Exception Handling** (try/except/else/finally) | nur ältere (SS23–WS2425) |

**→ Du weißt also sicher: A–E kommen. Nur *welche* Datenstruktur (D) und *welches* Sortierverfahren (E) ist die Unbekannte.**

---

## 2) Datenstrukturen – Matrix

| Klausur | Datenstruktur |
|---|---|
| SS23 | Einfach verkettete Liste (LinkedList) |
| WS2324 | **Stack** (LIFO) |
| SS24 | Binärer Suchbaum (BST) |
| WS2425 | Zirkuläre verkettete Liste (Circular Linked List) |
| SS25 | Ternärer Suchbaum (TST) |
| WS2526 | Trie (Präfixbaum) |

**Beobachtung:** Die **letzten drei** Klausuren (SS24 → SS25 → WS2526) waren **allesamt Bäume** (BST, TST, Trie). Ein Baum ein viertes Mal in Folge ist eher unwahrscheinlich.

### ❌ Datenstrukturen, die NIE drankamen
- **Queue / Warteschlange (FIFO)** ← größte Lücke bei den linearen Strukturen
- Doppelt verkettete Liste (Doubly Linked List)
- Heap als eigenständige Struktur

**→ Heißester Kandidat: Queue.** Sie ist der direkte Nachbar des Stacks (WS2324), quasi „Stack umgedreht", und wurde noch **nie** verlangt. Siehe Code in [`6_Fokusthemen_Bubble_Selection_Queue.md`](6_Fokusthemen_Bubble_Selection_Queue.md).

---

## 3) Sortierverfahren – Matrix

| Klausur | Sortierverfahren |
|---|---|
| SS23 | Quicksort |
| WS2324 | **Insertion-Sort** |
| SS24 | Mergesort |
| WS2425 | Quicksort |
| SS25 | **Heapsort** |
| WS2526 | Mergesort |

**Beobachtung:** Von den 6 gängigen Verfahren wurden **4** schon verwendet: Quicksort (2×), Mergesort (2×), Insertion-Sort, Heapsort.

### ❌ Sortierverfahren, die NIE drankamen
- **Bubble-Sort**
- **Selection-Sort**

**→ Heiße Kandidaten: Bubble-Sort und Selection-Sort.** Es sind die einzigen der „großen sechs", die noch fehlen – und die einfachsten. Beide werden aktuell in den SS26-Übungsblättern geübt. Code in [`6_Fokusthemen_Bubble_Selection_Queue.md`](6_Fokusthemen_Bubble_Selection_Queue.md).

> Immer gleiches Prinzip: das Sortierkriterium steckt **nur in der Vergleichszeile** – z. B. `len(a) > len(b)` (nach Länge) oder `(len(a), a) > (len(b), b)` (Länge, dann alphabetisch).

---

## 4) Theorie (Block A) – was schon dran war / Lücken

**Schon abgefragt:** 4+1-Sichtenmodell (Kruchten), Magisches Dreieck, funktionale vs. nicht-funktionale Anforderungen, Lasten-/Pflichtenheft, Qualitätsmerkmale (Benutzer/Entwickler), Stakeholder, Betriebskosten (~80 %) & Wartungsarten, versteckte Anforderungen, Programmiersprachen-Zweck.

**Selten / noch nicht (mögliche Lücken):**
- **Softwarekrise / CHAOS-Report** (Projektstatistiken)
- **Einführungsstrategien / Rollout** (Big-Bang, schrittweise, parallel, Pilot)
- **Brooks'sches Gesetz** („Mehr Personal macht ein spätes Projekt noch später") – wurde nur *nebenbei* erwähnt
- **1-10-100-Regel** (Fehlerkosten steigen je später entdeckt)
- **Vorgehensmodelle** im Detail (Wasserfall / V-Modell / Scrum-Ablauf)

---

## 5) Fazit – worauf du dich fokussieren solltest

**Sehr wahrscheinlich (Lücken, die „dran" sind):**
1. 🔥 **Queue (FIFO)** als Datenstruktur-Aufgabe
2. 🔥 **Bubble-Sort** oder **Selection-Sort** als Sortier-Aufgabe
3. Theorie: **Softwarekrise/CHAOS**, **Rollout-Strategien**, **1-10-100-Regel**, **Brooks**

**Trotzdem sicher beherrschen (kann als Variante wiederkommen):**
- Das **getopt-+-Datei-Muster** (kam in *jeder* Klausur, nur andere Verpackung)
- **Testen**: Äquivalenzklassen (Black-Box) **und** Pfadanalyse (White-Box) + pytest
- Als Baum-Absicherung: **BST** (falls doch wieder ein Baum kommt, ist BST der Standard)

**Weniger wahrscheinlich (aber Wissen soll sitzen):**
- Ein **vierter Baum** in Folge
- Eine **eigene Exception-Aufgabe** (in den letzten 2 Klausuren gestrichen)

---

### Ein-Satz-Merker
> **Skelett steht fest (Theorie · Testen · getopt+Datei · Datenstruktur · Sortieren).** Die einzige echte Unbekannte ist *welche* Datenstruktur und *welcher* Sort – und die stärksten Lücken heißen **Queue**, **Bubble-Sort**, **Selection-Sort**.
