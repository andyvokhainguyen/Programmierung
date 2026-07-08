"""
Übung 07: Exception Handling try/except/else/finally (WS2425/WS2324-Stil)

Hinweis: In DEINER Klausur wird das laut Ansage nicht direkt abgefragt -
trotzdem einmal üben, damit das Wissen sitzt.

Aufgabe: Wert an liste[index] durch eine Zahl teilen, drei Fehlerfälle sauber
abfangen (IndexError, ValueError, ZeroDivisionError).
"""


def teile_wert(liste, index, teiler):
    # ✍️ SELBST: try/except/else/finally aufbauen
    #   try:
    #       wert = liste[index]          # kann IndexError werfen
    #       zahl = int(teiler)           # kann ValueError werfen
    #       ergebnis = wert / zahl       # kann ZeroDivisionError werfen
    #   except IndexError:        print("Fehler: Index ausserhalb der Liste.")
    #   except ValueError:        print("Fehler: keine gültige Zahl.")
    #   except ZeroDivisionError: print("Fehler: Division durch Null.")
    #   else:                     print("Ergebnis:", ergebnis); return ergebnis   # nur ohne Fehler
    #   finally:                  print("Berechnung abgeschlossen.")               # IMMER
    try:
        wert = liste[index]
        zahl = int(teiler)
        ergebnis = wert / zahl
    except IndexError:
        print("Fehler: Index")
    except ValueError:
        print("Fehler: Keine gültige Zahl")
    except ZeroDivisionError:
        print("Fehler: Division durch Null")
    else:
        print("Ergebnis:", ergebnis)
        return ergebnis
    finally:
        print("Berechnungen abgeschlossen.")


# Testaufrufe
teile_wert([10, 20, 30], 1, "2")     # erwartet: Ergebnis: 10.0 + "abgeschlossen"
teile_wert([10, 20, 30], 5, "2")     # erwartet: Index-Fehler + "abgeschlossen"
teile_wert([10, 20, 30], 1, "0")     # erwartet: Division-durch-Null + "abgeschlossen"
teile_wert([10, 20, 30], 1, "x")     # erwartet: keine-gültige-Zahl + "abgeschlossen"
