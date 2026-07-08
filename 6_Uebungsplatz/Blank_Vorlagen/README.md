# ✍️ Blank-Vorlagen zum Selberschreiben

Ausführbare Übungsdateien, die **jedes Code-Thema aus den Zusammenfassungen genau einmal** abdecken. Es steht **nur der vom Professor vorgegebene Code** drin; überall wo `# ✍️ SELBST:` steht, schreibst du selbst (der Hinweis sagt, was hingehört).

## So übst du
1. Datei öffnen, an jedem `# ✍️ SELBST:` den Code aus dem Kopf schreiben (Hinweis nur bei Bedarf spicken).
2. Datei ausführen: `python3 <datei>.py` – unten steht ein Testaufruf **mit erwarteter Ausgabe als Kommentar**.
3. Vergleichen mit der Musterlösung:
   `../../2_Zusammenfassungen/3_Alle_Codes_zum_Abtippen.md` bzw. `7_Codes_Vorgabe_vs_Selbst.md`.

## Dateien (alle Themen abgedeckt)

**1) Testen**
| Datei | Thema |
|---|---|
| `01_testen_assertions.py` | defensive Assertions ergänzen |
| `02_testen_pytest.py` | pytest-Testfälle schreiben (`python3 -m pytest 02_testen_pytest.py`) |

**2) Kommandozeile + Datei-IO**
| Datei | Thema |
|---|---|
| `03_datei_lesen_schreiben.py` | Datei lesen/schreiben (`open`/`with`) |
| `04_sys_argv.py` | Argumente via `sys.argv` |
| `05_getopt_log.py` | Log-Tool mit **getopt** (Klausur-erlaubt) |
| `06_argparse_log.py` | Log-Tool mit **argparse** (Alternative) |
| `07_exceptions.py` | try/except/else/finally *(nicht direkt gefragt, aber Wissen)* |

**3) Datenstrukturen (Skript)**
| Datei | Thema |
|---|---|
| `08_linkedlist.py` | Einfach verkettete Liste (delete) |
| `09_stack_queue.py` | Stack (LIFO) & Queue (FIFO) |
| `10_bst.py` | Binärer Suchbaum (+ search, delete) |
| `11_doubly.py` | Doppelt verkettete Liste |

**4) Sortierverfahren**
| Datei | Thema |
|---|---|
| `12_sortierverfahren.py` | Bubble/Selection/Insertion/Quick/Merge/Heap |

**5) Zusatz: Datenstrukturen nur aus Altklausuren**
| Datei | Thema |
|---|---|
| `13_trie.py` | Trie / Präfixbaum (WS2526) |
| `14_ternaerer_suchbaum.py` | Ternärer Suchbaum (SS25) |
| `15_circular_list.py` | Zirkuläre Liste (WS2425) |

> Tipp: Bei Merge/Heap (`12`) ist die Hilfsfunktion (`merge`/`heapify`) schon vorgegeben – du schreibst nur die Hauptfunktion. Fang zum Üben mit `12` und `09` an (Bubble/Selection/Queue sind laut Lückenanalyse die heißesten Kandidaten).
